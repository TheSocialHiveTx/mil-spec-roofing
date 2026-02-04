import os
import re

def fix_schema_issues(file_path):
    """Fix common schema issues in HTML files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'application/ld+json' not in content:
            return False, "No schema found"
        
        original_content = content
        changes = []
        
        # Fix 1: Add postal code to addresses missing it (Webster, TX without postal code)
        pattern1 = r'"addressLocality":\s*"Webster",\s*"addressRegion":\s*"TX",\s*"addressCountry":\s*"US"'
        replacement1 = '"addressLocality": "Webster",\n        "addressRegion": "TX",\n        "postalCode": "77598",\n        "addressCountry": "US"'
        if re.search(pattern1, content):
            content = re.sub(pattern1, replacement1, content)
            changes.append("Added postal code 77598")
        
        # Fix 2: Add sameAs array to Organization nodes that are missing it
        # Find Organization blocks without sameAs
        org_pattern = r'("@type":\s*"Organization".*?)(("address":\s*{[^}]+}))'
        matches = list(re.finditer(org_pattern, content, re.DOTALL))
        
        for match in reversed(matches):  # Reverse to maintain positions
            org_block = match.group(0)
            if '"sameAs"' not in org_block:
                # Add sameAs array after address block
                same_as = ',\n      "sameAs": [\n        "https://www.facebook.com/MilSpecRoofing",\n        "https://www.instagram.com/milspec_roofing/",\n        "https://www.yelp.com/biz/mil-spec-roofing-and-construction-houston",\n        "https://www.homeadvisor.com/rated.MilSpecRoofing.100009058.html",\n        "https://nextdoor.com/pages/mil-spec-roofing-and-construction-houston-tx/"\n      ]'
                
                # Insert after the address block closing brace
                address_end = match.end(2)
                content = content[:address_end] + same_as + content[address_end:]
                changes.append("Added sameAs social links")
        
        # Fix 3: Add sameAs to LocalBusiness without it
        local_business_pattern = r'("@type":\s*"LocalBusiness".*?)(("address":\s*{[^}]+}))'
        matches = list(re.finditer(local_business_pattern, content, re.DOTALL))
        
        for match in reversed(matches):
            lb_block = match.group(0)
            if '"sameAs"' not in lb_block and '"sameAs"' not in content[match.start():match.start()+2000]:
                # Check if there's more content after address
                after_address = content[match.end():]
                # Find the next key or closing
                next_comma_or_brace = re.search(r'[,}]', after_address)
                if next_comma_or_brace:
                    insert_pos = match.end() + next_comma_or_brace.start()
                    same_as_lb = ',\n      "sameAs": [\n        "https://www.facebook.com/MilSpecRoofing",\n        "https://www.instagram.com/milspec_roofing/",\n        "https://www.yelp.com/biz/mil-spec-roofing-and-construction-houston",\n        "https://www.homeadvisor.com/rated.MilSpecRoofing.100009058.html",\n        "https://nextdoor.com/pages/mil-spec-roofing-and-construction-houston-tx/"\n      ]'
                    content = content[:insert_pos] + same_as_lb + content[insert_pos:]
                    if "Added sameAs" not in changes:
                        changes.append("Added sameAs to LocalBusiness")
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes
        
        return False, []
        
    except Exception as e:
        return False, f"Error: {e}"

# Process all HTML files
files_to_fix = []
for root, dirs, files in os.walk('.'):
    if 'images' in root or 'node_modules' in root:
        continue
    for file in files:
        if file == 'index.html':
            files_to_fix.append(os.path.join(root, file))

print("=" * 80)
print("FIXING SCHEMA ISSUES")
print("=" * 80)

fixed_count = 0
for file_path in sorted(files_to_fix):
    success, result = fix_schema_issues(file_path)
    if success:
        fixed_count += 1
        print(f"\n✓ {file_path}")
        for change in result:
            print(f"  • {change}")

print(f"\n{'=' * 80}")
print(f"✓ Fixed {fixed_count}/{len(files_to_fix)} files")
print("=" * 80)
