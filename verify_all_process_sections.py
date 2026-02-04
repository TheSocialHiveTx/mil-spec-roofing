import os
import re

# All 22 cities
cities = [
    'alvin', 'baytown', 'clear-lake', 'conroe', 'cypress', 'deer-park', 'friendswood', 'galveston',
    'houston', 'katy', 'kemah', 'la-porte', 'league-city', 'missouri-city', 'pasadena',
    'pearland', 'seabrook', 'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster'
]

print("FINAL VERIFICATION - Numbered Circle Process Sections")
print("=" * 75)

all_have_it = True

for city in cities:
    file_path = f'areas-served/{city}/index.html'
    if not os.path.exists(file_path):
        print(f'✗ {city.upper()}: File not found')
        all_have_it = False
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    city_name = city.replace('-', ' ').title()
    
    # Check for numbered circle (the blue circle with number 1)
    has_circle = bool(re.search(r'<div class="flex-shrink-0 w-16 h-16 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl">\s*1\s*</div>', content))
    
    # Check for process section heading
    has_heading = bool(re.search(rf'(Our|The).*{re.escape(city_name)}.*Process', content))
    
    if has_circle and has_heading:
        print(f'✅ {city.upper()}: Has numbered circle process section')
    elif has_circle:
        print(f'⚠️  {city.upper()}: Has circles but missing proper heading')
    else:
        print(f'❌ {city.upper()}: MISSING numbered circle process section')
        all_have_it = False

print("=" * 75)
if all_have_it:
    print('✅ SUCCESS: All 22 city pages now have numbered circle process sections!')
else:
    print('⚠️  Some pages need manual review')
