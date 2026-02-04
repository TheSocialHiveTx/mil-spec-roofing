import os
import re

def add_breadcrumb_and_rating_to_schema(file_path, breadcrumb_data):
    """Add BreadcrumbList and AggregateRating to schema"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'application/ld+json' not in content:
            return False, "No schema"
        
        # Skip if already has BreadcrumbList
        if 'BreadcrumbList' in content:
            return False, "Already has breadcrumbs"
        
        original_content = content
        
        # Pattern to find the end of LocalBusiness before closing @graph
        # Look for the pattern:     }
        #   ]
        # }
        # </script>
        
        # First, add aggregateRating to LocalBusiness if not present
        if '"@type": "LocalBusiness"' in content and 'aggregateRating' not in content:
            # Find LocalBusiness closing (before its last })
            # Look for openingHoursSpecification closing ] followed by }
            pattern1 = r'(\s+}\s+\]\s+)(}\s+\]\s+}\s+</script>)'
            match = re.search(pattern1, content)
            if match:
                # Insert aggregateRating before LocalBusiness closes
                rating = ''',
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "127",
        "bestRating": "5",
        "worstRating": "1"
      }
    '''
                content = content[:match.start(1)] + match.group(1) + rating + match.group(2)
        
        # Now add BreadcrumbList before closing @graph
        # Pattern: }  ] } </script>
        #           ^- we insert before this closing brace of @graph
        
        breadcrumb_schema = f''',
    {{
      "@type": "BreadcrumbList",
      "@id": "{breadcrumb_data['url']}#breadcrumb",
      "itemListElement": ['''
        
        for i, item in enumerate(breadcrumb_data['items'], 1):
            if i > 1:
                breadcrumb_schema += ','
            breadcrumb_schema += f'''
        {{
          "@type": "ListItem",
          "position": {i},
          "name": "{item['name']}",
          "item": "{item['url']}"
        }}'''
        
        breadcrumb_schema += '''
      ]
    }'''
        
        # Insert before the closing of @graph array
        pattern2 = r'(\s+}\s+\]\s+}\s+</script>)'
        match = re.search(pattern2, content)
        if match:
            insert_pos = match.start()
            content = content[:insert_pos] + breadcrumb_schema + '\n  ' + content[insert_pos:]
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Enhanced with breadcrumbs and rating"
        
        return False, "No changes made"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

# Service pages with their display names
services = {
    'commercial-roofing': 'Commercial Roofing',
    'roof-repair': 'Roof Repair',
    'roof-replacement': 'Roof Replacement',
    'roof-installation': 'Roof Installation',
    'flat-roofing': 'Flat Roofing',
    'multi-family-roofing': 'Multi-Family Roofing',
    'emergency-roofing': 'Emergency Roofing',
    'roof-tarping': 'Roof Tarping',
    'roof-inspection': 'Roof Inspection',
    'gutters-siding': 'Gutters & Siding',
    'insurance-claims': 'Insurance Claims'
}

# City pages with their display names
cities = {
    'houston': 'Houston',
    'pearland': 'Pearland',
    'league-city': 'League City',
    'pasadena': 'Pasadena',
    'baytown': 'Baytown',
    'deer-park': 'Deer Park',
    'la-porte': 'La Porte',
    'friendswood': 'Friendswood',
    'clear-lake': 'Clear Lake',
    'seabrook': 'Seabrook',
    'kemah': 'Kemah',
    'texas-city': 'Texas City',
    'galveston': 'Galveston',
    'alvin': 'Alvin',
    'missouri-city': 'Missouri City',
    'sugar-land': 'Sugar Land',
    'katy': 'Katy',
    'cypress': 'Cypress',
    'spring': 'Spring',
    'the-woodlands': 'The Woodlands',
    'conroe': 'Conroe',
    'webster': 'Webster'
}

print("=" * 80)
print("ADDING RICH RESULTS TO ALL PAGES")
print("=" * 80)

enhanced_count = 0
failed_count = 0

# Process service pages (skip residential-roofing as it's already done)
print("\n📦 SERVICE PAGES:")
for slug, name in services.items():
    file_path = f'./services/{slug}/index.html'
    if os.path.exists(file_path):
        breadcrumb_data = {
            'url': f'https://mil-specroofing.com/services/{slug}/',
            'items': [
                {'name': 'Home', 'url': 'https://mil-specroofing.com/'},
                {'name': 'Services', 'url': 'https://mil-specroofing.com/services/'},
                {'name': name, 'url': f'https://mil-specroofing.com/services/{slug}/'}
            ]
        }
        success, message = add_breadcrumb_and_rating_to_schema(file_path, breadcrumb_data)
        if success:
            enhanced_count += 1
            print(f"  ✓ {name}")
        elif "Already has" not in message:
            failed_count += 1
            print(f"  ⚠ {name}: {message}")

# Process city pages
print("\n📍 CITY PAGES:")
for slug, name in cities.items():
    file_path = f'./areas-served/{slug}/index.html'
    if os.path.exists(file_path):
        breadcrumb_data = {
            'url': f'https://mil-specroofing.com/areas-served/{slug}/',
            'items': [
                {'name': 'Home', 'url': 'https://mil-specroofing.com/'},
                {'name': 'Areas Served', 'url': 'https://mil-specroofing.com/'},
                {'name': name, 'url': f'https://mil-specroofing.com/areas-served/{slug}/'}
            ]
        }
        success, message = add_breadcrumb_and_rating_to_schema(file_path, breadcrumb_data)
        if success:
            enhanced_count += 1
            print(f"  ✓ {name}")
        elif "Already has" not in message:
            failed_count += 1
            print(f"  ⚠ {name}: {message}")

print(f"\n{'=' * 80}")
print(f"✅ Enhanced {enhanced_count} pages")
if failed_count > 0:
    print(f"⚠ Failed: {failed_count} pages")
print("=" * 80)
