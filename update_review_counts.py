import os

# Calculate weighted average: (11*5.0 + 7*5.0 + 3*4.3) / 21 = 4.9
# Total reviews: 11 + 7 + 3 = 21

pages = [
    'index.html',
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

for page in pages:
    if not os.path.exists(page):
        print(f"⚠️  Skipping {page} - file not found")
        continue
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update review count from 127 to 21
    # Keep rating at 4.9 (weighted average of 11@5.0 + 7@5.0 + 3@4.3 = 4.9)
    if '"reviewCount": "127"' in content:
        content = content.replace('"reviewCount": "127"', '"reviewCount": "21"')
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        
        fixed_count += 1
        print(f"✅ Updated {page}")

print(f"\n✅ Updated review count on {fixed_count} pages")
print(f"📊 Review breakdown: 11 Google (5.0★) + 7 Facebook (5.0★) + 3 Home Advisor (4.3★) = 21 total reviews")
print(f"⭐ Overall rating: 4.9/5.0")
