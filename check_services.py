import os

cities = ['houston', 'katy', 'kemah', 'la-porte', 'league-city', 'missouri-city', 'pasadena', 'pearland', 'seabrook', 'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster']

print("Checking for services section structure:")
print("=" * 50)

for city in cities:
    file_path = f'areas-served/{city}/index.html'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_section = '<section id="services"' in content
        has_grid = 'id="services-grid"' in content
        
        if has_section and has_grid:
            print(f'✅ {city.upper()}: OK')
        elif not has_section:
            print(f'❌ {city.upper()}: MISSING <section id="services">')
        elif not has_grid:
            print(f'❌ {city.upper()}: MISSING services-grid div')
