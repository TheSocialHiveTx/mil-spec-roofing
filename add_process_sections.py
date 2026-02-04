import os
import re

# Cities that need the numbered process section added
cities_to_add = [
    ('alvin', 'Alvin'),
    ('baytown', 'Baytown'),
    ('clear-lake', 'Clear Lake'),
    ('conroe', 'Conroe'),
    ('cypress', 'Cypress'),
    ('deer-park', 'Deer Park'),
    ('friendswood', 'Friendswood'),
    ('galveston', 'Galveston'),
    ('houston', 'Houston')
]

print("Adding numbered process sections to 9 city pages...")
print("=" * 75)

for city_slug, city_name in cities_to_add:
    file_path = f'areas-served/{city_slug}/index.html'
    if not os.path.exists(file_path):
        print(f'✗ {city_name.upper()}: File not found')
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it already has the numbered process
    if re.search(r'Our.*' + city_name + r'.*Process', content):
        print(f'✓ {city_name.upper()}: Already has process section')
        continue
    
    # Find the insertion point (before "How We Work" section)
    insertion_pattern = r'(</section>\s*<!-- Professionalism \+ Values.*?-->\s*<section class="py-20 bg-slate-100">)'
    
    # Create the numbered process section
    process_section = f'''
    <!-- Our {city_name} Process -->
    <section class="py-20 bg-white">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto">
          <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Our <span class="text-blue-600">{city_name} Roofing Process</span>
          </h2>
          <div class="h-1 w-20 bg-blue-600 rounded-full mb-6"></div>
          <p class="text-slate-600 text-lg leading-relaxed mb-12">
            Every roof repair in {city_name} and roof replacement in {city_name} project follows our proven military-precision process, ensuring quality results and clear communication throughout.
          </p>

          <div class="space-y-8">
            <div class="flex flex-col md:flex-row items-start gap-6">
              <div class="flex-shrink-0 w-16 h-16 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl">
                1
              </div>
              <div class="flex-grow">
                <h3 class="text-xl font-bold text-slate-900 mb-3">Comprehensive Inspection</h3>
                <p class="text-slate-600 leading-relaxed">
                  Our storm damage roof inspection in {city_name} begins with a thorough assessment of your roof's condition, identifying issues before they become major problems. We examine the entire roofing system, including decking, ventilation, and drainage.
                </p>
              </div>
            </div>

            <div class="flex flex-col md:flex-row items-start gap-6">
              <div class="flex-shrink-0 w-16 h-16 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl">
                2
              </div>
              <div class="flex-grow">
                <h3 class="text-xl font-bold text-slate-900 mb-3">Transparent Consultation</h3>
                <p class="text-slate-600 leading-relaxed">
                  We provide clear, honest recommendations with multiple options tailored to your {city_name} property and budget. No high-pressure sales tactics—just straightforward advice about the best solutions for your specific situation.
                </p>
              </div>
            </div>

            <div class="flex flex-col md:flex-row items-start gap-6">
              <div class="flex-shrink-0 w-16 h-16 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl">
                3
              </div>
              <div class="flex-grow">
                <h3 class="text-xl font-bold text-slate-900 mb-3">Precision Execution</h3>
                <p class="text-slate-600 leading-relaxed">
                  Our team executes every project with military discipline, ensuring clean work areas, proper safety protocols, and attention to detail that exceeds industry standards. We respect your property and neighborhood.
                </p>
              </div>
            </div>

            <div class="flex flex-col md:flex-row items-start gap-6">
              <div class="flex-shrink-0 w-16 h-16 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl">
                4
              </div>
              <div class="flex-grow">
                <h3 class="text-xl font-bold text-slate-900 mb-3">Quality Assurance</h3>
                <p class="text-slate-600 leading-relaxed">
                  Before we leave your {city_name} property, we conduct a final inspection and provide comprehensive documentation. Our work comes with warranties and our commitment to standing behind our craftsmanship.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

'''
    
    # Insert the new section before "How We Work"
    if re.search(insertion_pattern, content, re.DOTALL):
        content = re.sub(insertion_pattern, process_section + r'\1', content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✓ {city_name.upper()}: Added numbered process section')
    else:
        print(f'⚠ {city_name.upper()}: Could not find insertion point')

print("\n" + "=" * 75)
print("Process sections added!")
