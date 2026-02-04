import os
import json
import re

service_pages = [
    'services/residential-roofing/index.html',
    'services/commercial-roofing/index.html',
    'services/roof-repair/index.html',
    'services/roof-replacement/index.html',
    'services/roof-installation/index.html',
    'services/roof-inspection/index.html',
    'services/emergency-roofing/index.html',
    'services/flat-roofing/index.html',
    'services/gutters-siding/index.html',
    'services/insurance-claims/index.html',
    'services/multi-family-roofing/index.html',
    'services/roof-tarping/index.html'
]

fixed_count = 0

for page_path in service_pages:
    if not os.path.exists(page_path):
        print(f"⚠️  Skipping {page_path} - file not found")
        continue
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the JSON-LD script
    json_match = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', content, re.DOTALL)
    if not json_match:
        print(f"⚠️  No JSON-LD found in {page_path}")
        continue
    
    try:
        schema_data = json.loads(json_match.group(1))
        
        # Update each item in @graph
        for item in schema_data.get('@graph', []):
            # Remove streetAddress from address objects (it's empty and not needed)
            if '@type' in item and 'address' in item:
                if isinstance(item['address'], dict) and 'streetAddress' in item['address']:
                    del item['address']['streetAddress']
            
            # For LocalBusiness - remove duplicate areaServed
            if item.get('@type') == 'LocalBusiness':
                # Remove areaServed from LocalBusiness (already in Organization)
                if 'areaServed' in item:
                    del item['areaServed']
        
        # Convert back to JSON string
        new_json = json.dumps(schema_data, indent=2, ensure_ascii=False)
        
        # Replace in content
        new_content = content.replace(
            json_match.group(0),
            f'<script type="application/ld+json">\n{new_json}\n</script>'
        )
        
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        fixed_count += 1
        print(f"✅ Cleaned {page_path}")
        
    except json.JSONDecodeError as e:
        print(f"⚠️  JSON error in {page_path}: {e}")
        continue

print(f"\n✅ Cleaned schemas for {fixed_count} service pages")
print(f"🗑️  Removed empty streetAddress fields")
print(f"🔧 Removed duplicate areaServed from LocalBusiness")
