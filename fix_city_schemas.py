import os

def fix_city_schema_error(file_path):
    """Fix missing closing brace in city pages"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern: }  , { "@type": "BreadcrumbList"
        # Should be: } }  , { "@type": "BreadcrumbList"
        
        content = content.replace('    },\n    {\n      "@type": "BreadcrumbList"',
                                  '    }\n  ],\n    {\n      "@type": "BreadcrumbList"')
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

city_files = [f'./areas-served/{city}/index.html' for city in [
    'houston', 'pearland', 'league-city', 'pasadena', 'baytown', 'deer-park',
    'la-porte', 'friendswood', 'clear-lake', 'seabrook', 'kemah', 'texas-city',
    'galveston', 'alvin', 'missouri-city', 'sugar-land', 'katy', 'cypress',
    'spring', 'the-woodlands', 'conroe', 'webster'
]]

print("Fixing city page schemas...")
fixed = 0

for file_path in city_files:
    if os.path.exists(file_path):
        if fix_city_schema_error(file_path):
            fixed += 1
            city_name = os.path.basename(os.path.dirname(file_path))
            print(f"✓ {city_name}")

print(f"\n✅ Fixed {fixed} city pages")
