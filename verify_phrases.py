import os
import re

cities = ['houston', 'katy', 'kemah', 'la-porte', 'league-city', 'missouri-city', 'pasadena', 'pearland', 'seabrook', 'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster']

phrases = [
    'roofing contractor in',
    'roof repair in', 
    'roof replacement in',
    'storm damage roof inspection in'
]

print('FINAL VERIFICATION - City Pages Status:')
print('=' * 70)

all_pass = True
for city in cities:
    file_path = f'areas-served/{city}/index.html'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        city_name = city.replace('-', ' ').title()
        city_pass = True
        details = []
        
        for phrase in phrases:
            city_phrase = f'{phrase} {city_name}'
            count = len(re.findall(re.escape(city_phrase), content, re.IGNORECASE))
            if count < 2 or count > 4:
                city_pass = False
                all_pass = False
            status = '✓' if 2 <= count <= 4 else '✗'
            details.append(f'{status} {count}x')
        
        status_icon = '✅' if city_pass else '❌'
        print(f'{status_icon} {city.upper():15} - {" | ".join(details)}')

print('=' * 70)
if all_pass:
    print('✅ SUCCESS: All city pages verified and working correctly!')
else:
    print('❌ FAILED: Some pages need additional fixes.')
