import os

def fix_json_comma_error(file_path):
    """Fix the ]  , pattern that's causing JSON errors"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace ]  , with ],
        content = content.replace('      ]\n    ,\n      "aggregateRating"',
                                  '      ],\n      "aggregateRating"')
        
        # Replace }, { pattern between aggregateRating and BreadcrumbList
        content = content.replace('      },\n    {\n      "@type": "BreadcrumbList"',
                                  '      }\n    },\n    {\n      "@type": "BreadcrumbList"')
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error in {file_path}: {e}")
        return False

# Service pages
service_files = [
    './services/roof-tarping/index.html',
    './services/roof-replacement/index.html',
    './services/roof-repair/index.html',
    './services/roof-installation/index.html',
    './services/roof-inspection/index.html',
    './services/multi-family-roofing/index.html',
    './services/insurance-claims/index.html',
    './services/gutters-siding/index.html',
    './services/flat-roofing/index.html',
    './services/emergency-roofing/index.html'
]

# City pages
city_files = [f'./areas-served/{city}/index.html' for city in [
    'houston', 'pearland', 'league-city', 'pasadena', 'baytown', 'deer-park',
    'la-porte', 'friendswood', 'clear-lake', 'seabrook', 'kemah', 'texas-city',
    'galveston', 'alvin', 'missouri-city', 'sugar-land', 'katy', 'cypress',
    'spring', 'the-woodlands', 'conroe', 'webster'
]]

all_files = service_files + city_files

print("Fixing JSON comma errors...")
fixed = 0

for file_path in all_files:
    if os.path.exists(file_path):
        if fix_json_comma_error(file_path):
            fixed += 1
            print(f"✓ {os.path.basename(os.path.dirname(file_path))}")

print(f"\n✅ Fixed {fixed} files")
