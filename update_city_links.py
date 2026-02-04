#!/usr/bin/env python3
"""
Convert city name spans to clickable links across all pages
"""

import re
from pathlib import Path

# City mappings: display name -> URL slug
CITIES = {
    'Houston': 'houston',
    'Pasadena': 'pasadena',
    'Baytown': 'baytown',
    'Deer Park': 'deer-park',
    'La Porte': 'la-porte',
    'League City': 'league-city',
    'Pearland': 'pearland',
    'Friendswood': 'friendswood',
    'Clear Lake': 'clear-lake',
    'Seabrook': 'seabrook',
    'Kemah': 'kemah',
    'Texas City': 'texas-city',
    'Galveston': 'galveston',
    'Alvin': 'alvin',
    'Missouri City': 'missouri-city',
    'Sugar Land': 'sugar-land',
    'Katy': 'katy',
    'Cypress': 'cypress',
    'Spring': 'spring',
    'The Woodlands': 'the-woodlands',
    'Conroe': 'conroe',
    'Webster': 'webster'
}

def get_all_city_pages():
    """Get all city page HTML files."""
    areas_served_dir = Path('areas-served')
    if not areas_served_dir.exists():
        return []
    
    files = []
    for city_dir in areas_served_dir.iterdir():
        if city_dir.is_dir():
            index_file = city_dir / 'index.html'
            if index_file.exists():
                files.append(index_file)
    return files

def update_file(file_path):
    """Update city spans to links in a file."""
    if not file_path.exists():
        print(f"⚠️  Skipping {file_path} - file not found")
        return False
    
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    # Check if this section exists
    if 'bg-white px-4 py-2 rounded-full border border-slate-200 text-slate-700">Houston</span>' not in content:
        print(f"⚠️  Skipping {file_path} - city tags section not found")
        return False
    
    # Replace each city span with a link
    for city_name, slug in CITIES.items():
        # Pattern for single-line cities
        old_span = f'<span class="bg-white px-4 py-2 rounded-full border border-slate-200 text-slate-700">{city_name}</span>'
        new_link = f'<a href="/areas-served/{slug}/" class="bg-white px-4 py-2 rounded-full border border-slate-200 text-slate-700 hover:border-blue-500 hover:text-blue-600 hover:shadow-md transition-all cursor-pointer">{city_name}</a>'
        
        if old_span in content:
            content = content.replace(old_span, new_link)
    
    if content == original_content:
        print(f"⚠️  No changes made to {file_path}")
        return False
    
    file_path.write_text(content, encoding='utf-8')
    print(f"✅ Updated {file_path}")
    return True

def main():
    print("=" * 60)
    print("Converting City Spans to Clickable Links")
    print("=" * 60)
    
    # Get all city pages
    city_files = get_all_city_pages()
    print(f"\nFound {len(city_files)} city pages")
    
    success_count = 0
    for file_path in city_files:
        if update_file(file_path):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Successfully updated {success_count}/{len(city_files)} files")
    print("=" * 60)

if __name__ == '__main__':
    main()
