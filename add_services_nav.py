import os
import glob

# Services dropdown HTML
services_dropdown = '''
        <!-- Services Dropdown -->
        <div class="relative group">
          <a href="/services/"
            class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500 flex items-center gap-1 py-4">
            Services <i data-lucide="chevron-down" class="h-4 w-4"></i>
          </a>
          <div
            class="absolute left-0 top-full pt-2 w-72 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform origin-top-left z-50">
            <div
              class="bg-white shadow-xl rounded-lg border border-slate-100 overflow-hidden flex flex-col max-h-[80vh] overflow-y-auto">
              <a href="/services/residential-roofing/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Residential
                Roofing</a>
              <a href="/services/commercial-roofing/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Commercial
                Roofing</a>
              <a href="/services/roof-repair/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Repair</a>
              <a href="/services/roof-replacement/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Replacement</a>
              <a href="/services/roof-installation/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Installation</a>
              <a href="/services/flat-roofing/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Flat
                Roofing</a>
              <a href="/services/multi-family-roofing/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Multi-Family
                Roofing</a>
              <a href="/services/metal-roofing/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Metal
                Roofing</a>
              <a href="/services/emergency-roofing/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Emergency
                Roofing</a>
              <a href="/services/roof-tarping/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Tarping</a>
              <a href="/services/roof-inspection/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Inspection</a>
              <a href="/services/gutters-siding/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Gutters
                & Siding</a>
              <a href="/services/insurance-claims/"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Insurance
                Claims</a>
              <a href="/services/"
                class="block px-4 py-3 text-xs font-bold uppercase text-blue-600 bg-slate-50 hover:bg-slate-100 text-center sticky bottom-0">View
                All Services</a>
            </div>
          </div>
        </div>
'''

# Find all area pages
area_pages = glob.glob('areas-served/*/index.html')

fixed_count = 0

for page_path in area_pages:
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if Services dropdown is already present
    if 'Services <i data-lucide="chevron-down"' in content:
        print(f"⏭️  Skipping {page_path} - Services dropdown already present")
        continue
    
    # Find the position to insert (right after Home link, before Areas Served)
    home_link = '''        <a href="/"
          class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">Home</a>'''
    
    if home_link not in content:
        print(f"⚠️  Skipping {page_path} - Could not find Home link")
        continue
    
    # Insert Services dropdown after Home link
    new_content = content.replace(home_link, home_link + services_dropdown)
    
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    fixed_count += 1
    print(f"✅ Added Services dropdown to {page_path}")

print(f"\n✅ Added Services dropdown to {fixed_count} area pages")
print(f"🔍 Navigation now includes: Home > Services > Areas Served > General Construction > FAQ > Gallery > Contact")
