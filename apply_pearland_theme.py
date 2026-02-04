import os
import re

cities = [
    'houston', 'katy', 'kemah', 'la-porte', 'league-city', 'missouri-city', 'pasadena',
    'seabrook', 'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster'
]

print("Converting all city pages to match Pearland's design structure...")
print("=" * 70)

for city in cities:
    file_path = f'areas-served/{city}/index.html'
    if not os.path.exists(file_path):
        print(f'✗ {city}: File not found')
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes_made = []
    
    # 1. Replace check icons with check-circle icons in bullet lists
    if 'data-lucide="check"' in content:
        content = content.replace('data-lucide="check"', 'data-lucide="check-circle"')
        changes_made.append('Updated icons to check-circle')
    
    # 2. Update bullet list spacing
    content = re.sub(
        r'<ul class="text-slate-600 space-y-2">',
        '<ul class="space-y-3 text-slate-600">',
        content
    )
    if 'space-y-3' in content:
        changes_made.append('Updated bullet spacing')
    
    # 3. Update border colors from slate-200 to slate-100
    if 'border-slate-200' in content:
        content = content.replace('border-slate-200', 'border-slate-100')
        changes_made.append('Updated border colors')
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    if changes_made:
        print(f'✓ {city.upper()}: {", ".join(changes_made)}')
    else:
        print(f'○ {city.upper()}: No changes needed')

print("\n" + "=" * 70)
print("All pages updated to match Pearland's design!")
