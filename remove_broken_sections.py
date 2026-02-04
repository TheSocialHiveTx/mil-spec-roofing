#!/usr/bin/env python3
"""
Remove broken duplicate "Serving with Honor" sections from city pages.
These sections are missing proper wrappers and contain duplicate content.
"""

import re
from pathlib import Path

# Cities with broken duplicate sections
CITIES = [
    'pasadena', 'missouri-city', 'la-porte', 'kemah', 
    'league-city', 'houston', 'katy'
]

def remove_broken_section(city):
    """Remove the broken duplicate section from a city page."""
    file_path = Path(f'areas-served/{city}/index.html')
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return False
    
    content = file_path.read_text(encoding='utf-8')
    
    # Pattern to match the broken section (starts with just a div, no section wrapper)
    # It appears after </section> and before <section id="services"
    city_display = city.replace('-', ' ').title()
    
    pattern = re.compile(
        r'</section>\s*'  # End of previous section
        r'<div class="bg-slate-50[^>]*>\s*'  # The broken div that should be inside a section
        r'<h3[^>]*>Serving ' + re.escape(city_display) + r' with Honor</h3>.*?'  # Title
        r'</div>\s*'  # End of the broken div
        r'</div>\s*'  # Extra closing div
        r'</div>\s*'  # Extra closing div
        r'</section>\s*'  # Closing section that doesn't have an opening
        r'(?=<section id="services")',  # Lookahead to services section
        re.DOTALL
    )
    
    # Replace with just the section end
    new_content = pattern.sub('</section>\n    ', content)
    
    # Check if anything was changed
    if new_content == content:
        print(f"⚠️  No changes made to {city.upper()} - pattern may need adjustment")
        return False
    
    # Write back
    file_path.write_text(new_content, encoding='utf-8')
    print(f"✅ Removed broken section from {city.upper()}")
    return True

def main():
    print("=" * 60)
    print("Removing Broken Duplicate Sections")
    print("=" * 60)
    
    success_count = 0
    for city in CITIES:
        if remove_broken_section(city):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Successfully fixed {success_count}/{len(CITIES)} pages")
    print("=" * 60)

if __name__ == '__main__':
    main()
