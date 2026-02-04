import os

def fix_remaining_errors(file_path, fix_type):
    """Fix the remaining JSON errors"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        if fix_type == 'city':
            # Fix: }  ] newline  { should be }  ], newline  {
            content = content.replace('    }\n  ],\n    {\n      "@type": "BreadcrumbList"',
                                      '    }\n  ],\n  {\n      "@type": "BreadcrumbList"')
        elif fix_type == 'service':
            # Fix: extra } before ] } </script>
            content = content.replace('    }\n  \n    }\n  ]\n}',
                                      '    }\n  ]\n}')
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Fix city pages
cities = ['houston', 'pearland', 'league-city', 'pasadena', 'baytown', 'deer-park',
          'la-porte', 'friendswood', 'clear-lake', 'seabrook', 'kemah', 'texas-city',
          'galveston', 'alvin', 'missouri-city', 'sugar-land', 'katy', 'cypress',
          'spring', 'the-woodlands', 'conroe', 'webster']

print("Fixing city pages...")
fixed = 0
for city in cities:
    if fix_remaining_errors(f'./areas-served/{city}/index.html', 'city'):
        fixed += 1
        print(f"✓ {city}")

# Fix service pages
services = ['commercial-roofing', 'roof-repair', 'roof-replacement', 'roof-installation',
            'flat-roofing', 'multi-family-roofing', 'emergency-roofing', 'roof-tarping',
            'roof-inspection', 'gutters-siding', 'insurance-claims']

print("\nFixing service pages...")
for service in services:
    if fix_remaining_errors(f'./services/{service}/index.html', 'service'):
        fixed += 1
        print(f"✓ {service}")

print(f"\n✅ Fixed {fixed} pages total")
