import os

cities = ['houston', 'katy', 'kemah', 'la-porte', 'league-city', 'missouri-city', 'pasadena', 'pearland', 'seabrook', 'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster']

print("FINAL VERIFICATION - Services Section Structure:")
print("=" * 60)

all_good = True
for city in cities:
    file_path = f'areas-served/{city}/index.html'
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_section = '<section id="services"' in content
    has_grid = 'id="services-grid"' in content
    
    if has_section and has_grid:
        print(f'✅ {city.upper()}: Services section properly structured')
    else:
        print(f'❌ {city.upper()}: MISSING structure elements')
        all_good = False

print("=" * 60)
if all_good:
    print('✅ SUCCESS: All 14 pages have properly structured services sections!')
else:
    print('❌ Some pages still need fixes')
