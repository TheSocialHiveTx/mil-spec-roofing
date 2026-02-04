import os
import json
import re

# All cities served
cities_served = [
    "Houston", "Pearland", "League City", "Pasadena", "Baytown",
    "Deer Park", "La Porte", "Friendswood", "Clear Lake", "Seabrook",
    "Kemah", "Texas City", "Galveston", "Alvin", "Missouri City",
    "Sugar Land", "Katy", "Cypress", "Spring", "The Woodlands",
    "Conroe", "Webster"
]

# Create comprehensive areaServed array
areas_served = [
    {
        "@type": "City",
        "name": city,
        "containedIn": {
            "@type": "State",
            "name": "Texas"
        }
    }
    for city in cities_served
]

# Add geo coordinates for primary service area
geo_data = {
    "@type": "GeoCircle",
    "geoMidpoint": {
        "@type": "GeoCoordinates",
        "latitude": "29.5847",
        "longitude": "-95.1016"
    },
    "geoRadius": "40000"
}

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
        
        # Update Organization areaServed
        for item in schema_data.get('@graph', []):
            if item.get('@type') == 'Organization':
                item['areaServed'] = areas_served
                # Remove duplicate sameAs if exists
                if 'sameAs' in item:
                    seen = set()
                    unique_same_as = []
                    for url in item['sameAs']:
                        if url not in seen:
                            seen.add(url)
                            unique_same_as.append(url)
                    item['sameAs'] = unique_same_as
            
            # Update Service areaServed with cities + geocircle
            elif item.get('@type') == 'Service':
                item['areaServed'] = areas_served + [geo_data]
            
            # Update LocalBusiness areaServed
            elif item.get('@type') == 'LocalBusiness':
                item['areaServed'] = areas_served
                # Add geo coordinates
                item['geo'] = {
                    "@type": "GeoCoordinates",
                    "latitude": "29.5847",
                    "longitude": "-95.1016"
                }
        
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
        print(f"✅ Optimized {page_path}")
        
    except json.JSONDecodeError as e:
        print(f"⚠️  JSON error in {page_path}: {e}")
        continue

print(f"\n✅ Optimized schemas for {fixed_count} service pages")
print(f"📍 Added 22 cities to areaServed")
print(f"🗺️  Added GeoCircle with 40km radius around Houston")
print(f"📌 Added geo coordinates to LocalBusiness")
