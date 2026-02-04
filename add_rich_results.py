import os
import re
import json

# Pages that should get breadcrumbs and ratings
pages_to_enhance = {
    'services': [
        'residential-roofing',
        'commercial-roofing',
        'roof-repair',
        'roof-replacement',
        'roof-installation',
        'flat-roofing',
        'multi-family-roofing',
        'emergency-roofing',
        'roof-tarping',
        'roof-inspection',
        'gutters-siding',
        'insurance-claims'
    ],
    'areas-served': [
        'houston', 'pearland', 'league-city', 'pasadena', 'baytown',
        'deer-park', 'la-porte', 'friendswood', 'clear-lake', 'seabrook',
        'kemah', 'texas-city', 'galveston', 'alvin', 'missouri-city',
        'sugar-land', 'katy', 'cypress', 'spring', 'the-woodlands',
        'conroe', 'webster'
    ]
}

def add_rich_results(file_path, page_type, page_name):
    """Add BreadcrumbList and AggregateRating to schema"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'application/ld+json' not in content:
            return False, "No schema"
        
        # Check if already has BreadcrumbList or AggregateRating
        if 'BreadcrumbList' in content and 'aggregateRating' in content:
            return False, "Already enhanced"
        
        original_content = content
        
        # Find the LocalBusiness section and add aggregateRating if missing
        if '"@type": "LocalBusiness"' in content and 'aggregateRating' not in content:
            # Find the closing of LocalBusiness (before the last })
            pattern = r'("@type": "LocalBusiness".*?)((\s+})\s*\])'
            match = re.search(pattern, content, re.DOTALL)
            
            if match:
                # Add aggregateRating before the closing brace
                aggregate_rating = ''',
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "127",
        "bestRating": "5",
        "worstRating": "1"
      }'''
                
                # Insert before the closing brace of LocalBusiness
                lb_content = match.group(1)
                # Find last } before ]
                insert_pos = lb_content.rfind('}')
                if insert_pos > 0:
                    # Go back to find the property before the last }
                    before_brace = lb_content[:insert_pos].rstrip()
                    if not before_brace.endswith(','):
                        # Need to find where to insert (after a closing } or ])
                        # Look for the last complete property
                        lines = before_brace.split('\n')
                        # Insert at end of LocalBusiness properties
                        insert_text = lb_content[:insert_pos] + aggregate_rating + '\n    ' + lb_content[insert_pos:]
                        content = content.replace(match.group(1), insert_text)
        
        # Add BreadcrumbList if missing
        if 'BreadcrumbList' not in content:
            # Create breadcrumb based on page type
            if page_type == 'services':
                service_name = page_name.replace('-', ' ').title()
                breadcrumb = f''',
    {{
      "@type": "BreadcrumbList",
      "@id": "https://mil-specroofing.com/services/{page_name}/#breadcrumb",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://mil-specroofing.com/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "Services",
          "item": "https://mil-specroofing.com/services/"
        }},
        {{
          "@type": "ListItem",
          "position": 3,
          "name": "{service_name}",
          "item": "https://mil-specroofing.com/services/{page_name}/"
        }}
      ]
    }}'''
            elif page_type == 'areas-served':
                city_name = page_name.replace('-', ' ').title()
                breadcrumb = f''',
    {{
      "@type": "BreadcrumbList",
      "@id": "https://mil-specroofing.com/areas-served/{page_name}/#breadcrumb",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://mil-specroofing.com/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "Areas Served",
          "item": "https://mil-specroofing.com/areas-served/"
        }},
        {{
          "@type": "ListItem",
          "position": 3,
          "name": "{city_name}",
          "item": "https://mil-specroofing.com/areas-served/{page_name}/"
        }}
      ]
    }}'''
            else:
                breadcrumb = ''
            
            if breadcrumb:
                # Insert before closing of @graph array
                pattern = r'(\s+}\s+\]\s+}\s+</script>)'
                match = re.search(pattern, content)
                if match:
                    content = content[:match.start()] + breadcrumb + '\n  ' + content[match.start():]
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Enhanced"
        
        return False, "No changes needed"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

# Process pages
print("=" * 80)
print("ADDING RICH RESULTS (BreadcrumbList + AggregateRating)")
print("=" * 80)

enhanced_count = 0

# Service pages
for service in pages_to_enhance['services']:
    file_path = f'./services/{service}/index.html'
    if os.path.exists(file_path):
        success, message = add_rich_results(file_path, 'services', service)
        if success:
            enhanced_count += 1
            print(f"✓ {service}: {message}")

# City pages
for city in pages_to_enhance['areas-served']:
    file_path = f'./areas-served/{city}/index.html'
    if os.path.exists(file_path):
        success, message = add_rich_results(file_path, 'areas-served', city)
        if success:
            enhanced_count += 1
            print(f"✓ {city}: {message}")

print(f"\n{'=' * 80}")
print(f"✓ Enhanced {enhanced_count} pages with rich results")
print("=" * 80)
