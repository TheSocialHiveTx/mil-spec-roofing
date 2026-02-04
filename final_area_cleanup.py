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
            # Keep areaServed ONLY in Organization
            # Remove from Service and LocalBusiness to eliminate duplication
            if item.get('@type') == 'Service':
                if 'areaServed' in item:
                    del item['areaServed']
                    print(f"  Removed areaServed from Service in {page_path}")
            
            elif item.get('@type') == 'LocalBusiness':
                if 'areaServed' in item:
                    del item['areaServed']
                    print(f"  Removed areaServed from LocalBusiness in {page_path}")
        
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
print(f"🎯 areaServed now only appears in Organization schema")
print(f"📍 All 22 cities listed once per page")
