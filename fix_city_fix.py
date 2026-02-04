import os

def fix_city_schema(file_path):
    """Fix the comma issue before BreadcrumbList"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix pattern: },  with newline then { "@type": "BreadcrumbList"
        # Should have proper closing
        content = content.replace('      "areaServed": { "@type": "AdministrativeArea", "name": "Southeast Texas" },\n    {\n      "@type": "BreadcrumbList"',
                                  '      "areaServed": { "@type": "AdministrativeArea", "name": "Southeast Texas" }\n    }\n  ],\n    {\n      "@type": "BreadcrumbList"')
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

cities = ['houston', 'pearland', 'league-city', 'pasadena', 'baytown', 'deer-park',
          'la-porte', 'friendswood', 'clear-lake', 'seabrook', 'kemah', 'texas-city',
          'galveston', 'alvin', 'missouri-city', 'sugar-land', 'katy', 'cypress',
          'spring', 'the-woodlands', 'conroe', 'webster']

print("Fixing city schemas...")
fixed = 0

for city in cities:
    file_path = f'./areas-served/{city}/index.html'
    if os.path.exists(file_path):
        if fix_city_schema(file_path):
            fixed += 1
            print(f"✓ {city}")

print(f"\n✅ Fixed {fixed} city pages")
