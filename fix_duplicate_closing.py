import os
import re

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
    
    # Pattern to find duplicate closing tags after services section
    # This matches when we have closing tags duplicated
    pattern = r'(</a>\s+</div>\s+</div>\s+</section>)\s+(</div>\s+</div>\s+</section>)'
    
    # Replace with single instance
    content = re.sub(pattern, r'\1', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ {city}: Fixed duplicate closing tags')

print('\nAll duplicate closing tags removed!')
