import os
import re

# All 22 cities
cities = [
    'alvin', 'baytown', 'clear-lake', 'conroe', 'cypress', 'deer-park', 'friendswood', 'galveston',
    'houston', 'katy', 'kemah', 'la-porte', 'league-city', 'missouri-city', 'pasadena',
    'pearland', 'seabrook', 'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster'
]

print("Converting ALL 22 city pages to numbered circle process format...")
print("=" * 75)

for city in cities:
    file_path = f'areas-served/{city}/index.html'
    if not os.path.exists(file_path):
        print(f'✗ {city.upper()}: File not found')
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    city_name = city.replace('-', ' ').title()
    
    # Check if already has numbered circle format
    if re.search(r'<div class="flex-shrink-0 w-16 h-16 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl">\s*1\s*</div>', content):
        print(f'✓ {city.upper()}: Already has numbered circle format')
        continue
    
    # Find the section with boxes (bg-slate-50 border border-slate-100 rounded-lg p-6)
    # and replace with numbered circles
    box_pattern = r'(<div class="space-y-8">)\s*(<div class="bg-slate-50 border border-slate-100 rounded-lg p-6">.*?</div>\s*</div>)\s*(</div>)'
    
    # Check if it has the box format
    if re.search(r'<div class="bg-slate-50 border border-slate-100 rounded-lg p-6">', content, re.DOTALL):
        # Find all boxes and convert them
        # Pattern to match each box
        box_item_pattern = r'<div class="bg-slate-50 border border-slate-100 rounded-lg p-6">\s*<h3 class="text-xl font-bold text-slate-900 mb-3">(.*?)</h3>\s*<p class="text-slate-600">\s*(.*?)\s*</p>\s*</div>'
        
        # Find all matches
        boxes = re.findall(box_item_pattern, content, re.DOTALL)
        
        if boxes and len(boxes) >= 3:
            # Build the numbered circle version
            numbered_html = '<div class="space-y-8">\n'
            for i, (title, description) in enumerate(boxes, 1):
                numbered_html += f'''            <div class="flex flex-col md:flex-row items-start gap-6">
              <div class="flex-shrink-0 w-16 h-16 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl">
                {i}
              </div>
              <div class="flex-grow">
                <h3 class="text-xl font-bold text-slate-900 mb-3">{title}</h3>
                <p class="text-slate-600 leading-relaxed">
                  {description.strip()}
                </p>
              </div>
            </div>

'''
            numbered_html += '          </div>'
            
            # Replace the entire space-y-8 section with boxes
            pattern_to_replace = r'<div class="space-y-8">.*?(?=</div>\s*</div>\s*</div>\s*</section>)'
            content = re.sub(pattern_to_replace, numbered_html, content, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f'✓ {city.upper()}: Converted from boxes to numbered circles ({len(boxes)} steps)')
        else:
            print(f'⚠ {city.upper()}: Has boxes but unexpected format ({len(boxes)} boxes found)')
    else:
        print(f'○ {city.upper()}: Different format - needs manual review')

print("\n" + "=" * 75)
print("Conversion complete!")
