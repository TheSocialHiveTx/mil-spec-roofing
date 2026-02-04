import os

def fix_breadcrumb_placement(file_path):
    """Fix breadcrumb should be in @graph array"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern: }  ],  { "@type": "BreadcrumbList"
        # Should be: },  { "@type": "BreadcrumbList" ... (still in array)
        content = content.replace('    }\n  ],\n  {\n      "@type": "BreadcrumbList"',
                                  '    },\n    {\n      "@type": "BreadcrumbList"')
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

cities = ['pearland', 'league-city', 'pasadena', 'baytown', 'deer-park',
          'la-porte', 'friendswood', 'clear-lake', 'seabrook', 'kemah', 'texas-city',
          'galveston', 'alvin', 'missouri-city', 'sugar-land', 'katy', 'cypress',
          'spring', 'the-woodlands', 'conroe', 'webster']

print("Fixing breadcrumb placement in city pages...")
fixed = 0

for city in cities:
    if fix_breadcrumb_placement(f'./areas-served/{city}/index.html'):
        fixed += 1
        print(f"✓ {city}")

print(f"\n✅ Fixed {fixed} city pages")
