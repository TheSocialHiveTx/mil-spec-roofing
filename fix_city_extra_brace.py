import os
import re

city_pages = [
    'alvin', 'baytown', 'clear-lake', 'conroe', 'cypress', 'deer-park',
    'friendswood', 'galveston', 'houston', 'katy', 'kemah', 'la-porte',
    'league-city', 'missouri-city', 'pasadena', 'pearland', 'seabrook',
    'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster'
]

for city in city_pages:
    file_path = f'areas-served/{city}/index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the extra } that appears after the BreadcrumbList closing
    # Pattern: }  ]  }  (extra brace)  ]  }
    # Should be: }  ]  ]  }
    content = re.sub(
        r'(\s*}\s*\]\s*)\}\s*(\]\s*})',
        r'\1\2',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"✅ Fixed {len(city_pages)} city pages")
