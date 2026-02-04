import os

cities = [
    'houston', 'katy', 'kemah', 'la-porte', 'league-city', 'missouri-city', 'pasadena',
    'pearland', 'seabrook', 'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster'
]

print("FINAL VERIFICATION - Checking design consistency across all city pages")
print("=" * 75)

all_consistent = True

for city in cities:
    file_path = f'areas-served/{city}/index.html'
    if not os.path.exists(file_path):
        print(f'✗ {city.upper()}: File not found')
        all_consistent = False
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        'check-circle icons': 'data-lucide="check-circle"' in content,
        'space-y-3 spacing': 'space-y-3 text-slate-600' in content or 'space-y-3' in content,
        'slate-100 borders': 'border-slate-100' in content
    }
    
    issues = [k for k, v in checks.items() if not v]
    
    if not issues:
        print(f'✅ {city.upper()}: All design elements match Pearland')
    else:
        print(f'⚠️  {city.upper()}: Missing - {", ".join(issues)}')
        all_consistent = False

print("=" * 75)
if all_consistent:
    print('✅ SUCCESS: All city pages now have consistent design matching Pearland!')
    print('\nDesign elements applied:')
    print('  • Check-circle icons in bullet lists')
    print('  • Consistent space-y-3 spacing')
    print('  • Slate-100 border colors')
else:
    print('⚠️  Some pages may need manual review')
