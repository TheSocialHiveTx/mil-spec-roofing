import os
import re

# All area pages
area_dirs = [d for d in os.listdir('areas-served') if os.path.isdir(os.path.join('areas-served', d))]

fixed_count = 0

for city in area_dirs:
    file_path = f'areas-served/{city}/index.html'
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the desktop menu div to use better spacing
    old_pattern = r'<div class="hidden lg:flex space-x-6 items-center" id="desktop-menu">'
    new_pattern = '<div class="hidden lg:flex space-x-4 xl:space-x-6 items-center flex-wrap" id="desktop-menu">'
    
    if old_pattern in content:
        new_content = content.replace(old_pattern, new_pattern)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        fixed_count += 1
        print(f"✅ Fixed navbar spacing in {city}")
    else:
        print(f"⏭️  Skipping {city} - different navbar structure")

print(f"\n✅ Fixed {fixed_count} area pages")
print(f"📐 Reduced spacing from space-x-6 to space-x-4 on large screens")
print(f"📐 Added flex-wrap to prevent overflow")
