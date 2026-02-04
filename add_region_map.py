import os

root_dir = os.getcwd()
services_dir = os.path.join(root_dir, 'services')

# Google Map for Southeast Texas (Houston and surrounding)
# Centered roughly on Houston with a zoom level that shows the region
map_html = """
    <!-- Regional Map -->
    <section class="py-16 bg-slate-50 border-t border-slate-200">
        <div class="container mx-auto px-4">
            <div class="text-center mb-10">
                <h2 class="text-3xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
                    Serving All of <span class="text-blue-600">Southeast Texas</span>
                </h2>
                <div class="h-1 w-20 bg-blue-600 mx-auto rounded-full mb-6"></div>
                <p class="text-slate-600 max-w-2xl mx-auto">
                    From Houston to Galveston, and everywhere in between. Our teams are deployed across the region.
                </p>
            </div>
            <div class="w-full h-[450px] bg-slate-200 rounded-xl overflow-hidden shadow-lg border border-slate-300">
                <iframe 
                    src="https://maps.google.com/maps?width=100%25&height=600&hl=en&q=Southeast%20Texas%20Houston&t=&z=9&ie=UTF8&iwloc=B&output=embed" 
                    width="100%" 
                    height="100%" 
                    style="border:0;" 
                    allowfullscreen="" 
                    loading="lazy">
                </iframe>
            </div>
        </div>
    </section>
"""

# Walk through services directory
target_files = []
# Add Homepage
target_files.append(os.path.join(root_dir, 'index.html'))

# Add Services Pages
for root, dirs, files in os.walk(services_dir):
    for file in files:
        if file == 'index.html':
            target_files.append(os.path.join(root, file))

for file_path in target_files:
    # Read content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicates (checking for the specific comment or header content)
    if "<!-- Regional Map -->" in content or "Serving All of <span class=\"text-blue-600\">Southeast Texas</span>" in content:
        print(f"Skipping {file_path} - Map already present.")
        continue

    # Target injection point: Before Footer
    # We look for <footer class="bg-slate-950...
    # Or just <footer
    
    if '<footer' in content:
        # Use regex split to ensure we don't break if multiple footers (unlikely) but safer to just split once
        parts = content.split('<footer', 1) 
        new_content = parts[0] + map_html + '\n    <footer' + parts[1]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected map into: {file_path}")
    else:
        print(f"Warning: Could not find footer in {file_path}")
