import os

cities = [
    'houston', 'katy', 'kemah', 'la-porte', 'league-city', 'missouri-city', 'pasadena',
    'pearland', 'seabrook', 'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster'
]

for city in cities:
    file_path = f'areas-served/{city}/index.html'
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove duplicate closing section tag
    content = content.replace('    </section>    </section>', '    </section>')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ {city}: Removed duplicate closing section tag')

print('\nAll duplicate tags removed!')
