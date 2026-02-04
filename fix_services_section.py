import os
import re

cities = [
    'houston', 'katy', 'kemah', 'la-porte', 'league-city', 'missouri-city', 'pasadena',
    'pearland', 'seabrook', 'spring', 'sugar-land', 'texas-city', 'the-woodlands', 'webster'
]

for city in cities:
    file_path = f'areas-served/{city}/index.html'
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has section wrapper
    if '<section id="services"' in content:
        print(f'✓ {city}: Already has section wrapper')
        continue
    
    # Find the first service card (Roof Repair)
    match = re.search(r'(\s*<!-- ✅ Roof Repair -->)', content)
    if not match:
        print(f'✗ {city}: Could not find Roof Repair card')
        continue
    
    # Get the city name formatted
    city_name = city.replace('-', ' ').title()
    
    # Create the section opening
    section_opening = f'''    </section>
    <section id="services" class="py-24 bg-white relative">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Roofing <span class="text-blue-600">Services in {city_name}</span>
          </h2>
          <div class="h-1 w-20 bg-blue-600 mx-auto rounded-full mb-6"></div>
          <p class="text-slate-600 max-w-2xl mx-auto text-lg">
            We are known for fast diagnostics and straightforward options. If you need roof repair in {city_name}, we track the leak source, repair the failure point, and confirm drainage performance. When roof replacement in {city_name} is the smarter long-term move, we build a full system designed to handle wind and moisture.
          </p>
        </div>

        <div id="services-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

'''
    
    # Insert before the first service card
    content = content.replace(match.group(1), section_opening + match.group(1))
    
    # Now find the last service card (Insurance Claims Assistance) closing tag and add closing divs
    # Find the closing </a> of the Insurance Claims card
    insurance_pattern = r'(<!-- ✅ Insurance Claims Assistance -->.*?</a>)'
    insurance_match = re.search(insurance_pattern, content, re.DOTALL)
    
    if insurance_match:
        # Add closing tags after the Insurance card
        closing_tags = '''

        </div>
      </div>
    </section>'''
        content = content.replace(insurance_match.group(1), insurance_match.group(1) + closing_tags)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ {city}: Fixed services section structure')

print('\nAll pages fixed!')
