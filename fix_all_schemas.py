import os
import re

def fix_schema_formatting(file_path):
    """Fix the JSON syntax error in schema"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix the pattern: ]  ,  "aggregateRating" ... }, {
        # Should be: ], "aggregateRating" ... } }, {
        
        # Pattern to find and fix
        pattern = r'(\s+}\s+\]\s+),(\s+"aggregateRating":\s+\{[^}]+}\s+),(\s+\{\s+"@type": "BreadcrumbList")'
        
        replacement = r'\1,\2}\n  },\n  \3'
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Fixed"
        return False, "No change"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

# Files to fix
files = []

# Service pages
for service in ['roof-repair', 'roof-replacement', 'roof-installation', 'flat-roofing',
                'multi-family-roofing', 'emergency-roofing', 'roof-tarping',
                'roof-inspection', 'gutters-siding', 'insurance-claims']:
    files.append(f'./services/{service}/index.html')

# City pages
for city in ['houston', 'pearland', 'league-city', 'pasadena', 'baytown', 'deer-park',
             'la-porte', 'friendswood', 'clear-lake', 'seabrook', 'kemah', 'texas-city',
             'galveston', 'alvin', 'missouri-city', 'sugar-land', 'katy', 'cypress',
             'spring', 'the-woodlands', 'conroe', 'webster']:
    files.append(f'./areas-served/{city}/index.html')

print("Fixing JSON syntax errors...")
fixed_count = 0

for file_path in files:
    if os.path.exists(file_path):
        success, msg = fix_schema_formatting(file_path)
        if success:
            fixed_count += 1
            print(f"✓ {file_path}")

print(f"\n✓ Fixed {fixed_count}/{len(files)} files")
