import os

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
    
    # Remove the standalone } after BreadcrumbList
    # Pattern: ]  }  (blank line)  }  ]  }
    # Should be: ]  }  ]  }
    content = content.replace('      ]\n    }\n  \n    }\n  ]\n}', '      ]\n    }\n  ]\n}')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"✅ Fixed {len(city_pages)} city pages - removed extra closing brace")
