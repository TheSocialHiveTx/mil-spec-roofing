import os
import json
import re

def extract_schema(content):
    """Extract JSON-LD schema from HTML content"""
    pattern = r'<script type="application/ld\+json">(.*?)</script>'
    matches = re.findall(pattern, content, re.DOTALL)
    schemas = []
    for match in matches:
        try:
            schema = json.loads(match.strip())
            schemas.append(schema)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
    return schemas

def check_file_schema(file_path):
    """Check the schema in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'application/ld+json' not in content:
            return {'has_schema': False}
        
        schemas = extract_schema(content)
        
        result = {
            'has_schema': True,
            'schema_count': len(schemas),
            'issues': []
        }
        
        for schema in schemas:
            # Check for Organization
            if '@graph' in schema:
                for item in schema['@graph']:
                    if item.get('@type') == 'Organization' or item.get('@type') == 'LocalBusiness':
                        address = item.get('address', {})
                        if isinstance(address, dict):
                            locality = address.get('addressLocality', '')
                            region = address.get('addressRegion', '')
                            postal = address.get('postalCode', '')
                            street = address.get('streetAddress', '')
                            
                            # Check for inconsistencies
                            if locality == 'Houston' and not street:
                                result['issues'].append('Has Houston but missing street address')
                            elif locality == 'Webster' and street:
                                result['issues'].append('Has Webster with street address (should be Houston)')
                            elif not postal:
                                result['issues'].append('Missing postal code')
                                
                        # Check sameAs links
                        same_as = item.get('sameAs', [])
                        if len(same_as) < 5:
                            result['issues'].append(f'Only {len(same_as)} social links (expected 5)')
        
        return result
        
    except Exception as e:
        return {'error': str(e)}

# Check all HTML files
print("=" * 80)
print("SCHEMA VERIFICATION REPORT")
print("=" * 80)

files_to_check = []
for root, dirs, files in os.walk('.'):
    if 'images' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('index.html'):
            files_to_check.append(os.path.join(root, file))

files_with_issues = []
files_without_schema = []

for file_path in sorted(files_to_check):
    result = check_file_schema(file_path)
    
    if 'error' in result:
        print(f"\n❌ ERROR: {file_path}")
        print(f"   {result['error']}")
    elif not result['has_schema']:
        files_without_schema.append(file_path)
    elif result['issues']:
        files_with_issues.append((file_path, result['issues']))

print(f"\n✓ Total files checked: {len(files_to_check)}")
print(f"✓ Files with schema: {len(files_to_check) - len(files_without_schema)}")
print(f"✓ Files without schema: {len(files_without_schema)}")
print(f"⚠ Files with issues: {len(files_with_issues)}")

if files_without_schema:
    print("\n" + "=" * 80)
    print("FILES WITHOUT SCHEMA:")
    print("=" * 80)
    for file_path in files_without_schema:
        print(f"  • {file_path}")

if files_with_issues:
    print("\n" + "=" * 80)
    print("FILES WITH SCHEMA ISSUES:")
    print("=" * 80)
    for file_path, issues in files_with_issues:
        print(f"\n📄 {file_path}")
        for issue in issues:
            print(f"   ⚠ {issue}")

print("\n" + "=" * 80)
print("RECOMMENDATIONS:")
print("=" * 80)
print("""
1. ✓ All pages should have JSON-LD schema markup
2. ✓ Use consistent address: Webster, TX 77598 (no street address)
3. ✓ Include all 5 social media links in sameAs array
4. ✓ Each page should have appropriate @type (WebPage, Service, FAQPage, etc.)
5. ✓ Include proper OpenGraph and meta tags alongside schema
""")
