import os
import re

def fix_json_syntax_errors(file_path):
    """Fix JSON syntax errors from previous script"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix pattern: ]  ,  "aggregateRating"
        # Should be: ] }, "aggregateRating" needs to be in a new object
        
        # The issue is we added aggregateRating as a property of LocalBusiness
        # but we need to close LocalBusiness first, then add BreadcrumbList as a separate object
        
        # Fix pattern 1: Remove incorrect comma after ]
        content = re.sub(r'(\s+\]\s+),(\s+"aggregateRating")', r'\1\2', content)
        
        # Fix pattern 2: Close LocalBusiness properly before breadcrumb
        # Pattern: aggregateRating closing }  ,  BreadcrumbList opening {
        # Should have closing } for LocalBusiness
        pattern1 = r'("worstRating": "1"\s+}\s+)(},\s+{\s+"@type": "BreadcrumbList")'
        content = re.sub(pattern1, r'\1}\n  ],\n  {  "@type": "BreadcrumbList"', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

# Get all affected files
files_to_fix = []

# Service pages
services = ['commercial-roofing', 'roof-repair', 'roof-replacement', 'roof-installation',
            'flat-roofing', 'multi-family-roofing', 'emergency-roofing', 'roof-tarping',
            'roof-inspection', 'gutters-siding', 'insurance-claims']

for service in services:
    path = f'./services/{service}/index.html'
    if os.path.exists(path):
        files_to_fix.append(path)

# City pages
cities = ['houston', 'pearland', 'league-city', 'pasadena', 'baytown', 'deer-park',
          'la-porte', 'friendswood', 'clear-lake', 'seabrook', 'kemah', 'texas-city',
          'galveston', 'alvin', 'missouri-city', 'sugar-land', 'katy', 'cypress',
          'spring', 'the-woodlands', 'conroe', 'webster']

for city in cities:
    path = f'./areas-served/{city}/index.html'
    if os.path.exists(path):
        files_to_fix.append(path)

print("Fixing JSON syntax errors...")
fixed = 0
for file_path in files_to_fix:
    if fix_json_syntax_errors(file_path):
        fixed += 1

print(f"✓ Fixed {fixed}/{len(files_to_fix)} files")
