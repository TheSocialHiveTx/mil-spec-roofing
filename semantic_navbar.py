import os
import re

# Semantic navigation HTML with proper ARIA attributes and ul/li structure
semantic_nav = '''      <ul class="hidden lg:flex space-x-4 xl:space-x-6 items-center flex-wrap list-none m-0 p-0" id="desktop-menu" role="menubar">
        <li role="none">
          <a href="/" role="menuitem"
            class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">Home</a>
        </li>
        
        <!-- Services Dropdown -->
        <li class="relative group" role="none">
          <a href="/services/" role="menuitem" aria-haspopup="true" aria-expanded="false"
            class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500 flex items-center gap-1 py-4">
            Services <i data-lucide="chevron-down" class="h-4 w-4" aria-hidden="true"></i>
          </a>
          <ul role="menu" aria-label="Services Menu"
            class="absolute left-0 top-full pt-2 w-72 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform origin-top-left z-50 list-none m-0 p-0">
            <li role="none"
              class="bg-white shadow-xl rounded-lg border border-slate-100 overflow-hidden flex flex-col max-h-[80vh] overflow-y-auto">
              <a href="/services/residential-roofing/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Residential
                Roofing</a>
              <a href="/services/commercial-roofing/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Commercial
                Roofing</a>
              <a href="/services/roof-repair/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Repair</a>
              <a href="/services/roof-replacement/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Replacement</a>
              <a href="/services/roof-installation/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Installation</a>
              <a href="/services/flat-roofing/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Flat
                Roofing</a>
              <a href="/services/multi-family-roofing/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Multi-Family
                Roofing</a>
              <a href="/services/metal-roofing/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Metal
                Roofing</a>
              <a href="/services/emergency-roofing/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Emergency
                Roofing</a>
              <a href="/services/roof-tarping/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Tarping</a>
              <a href="/services/roof-inspection/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof
                Inspection</a>
              <a href="/services/gutters-siding/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Gutters
                & Siding</a>
              <a href="/services/insurance-claims/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Insurance
                Claims</a>
              <a href="/services/" role="menuitem"
                class="block px-4 py-3 text-xs font-bold uppercase text-blue-600 bg-slate-50 hover:bg-slate-100 text-center sticky bottom-0">View
                All Services</a>
            </li>
          </ul>
        </li>

        <!-- Areas Served Dropdown -->
        <li class="relative group" role="none">
          <a href="/areas-served/" role="menuitem" aria-haspopup="true" aria-expanded="false"
            class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500 flex items-center gap-1 py-4">
            Areas Served <i data-lucide="chevron-down" class="h-4 w-4" aria-hidden="true"></i>
          </a>
          <ul role="menu" aria-label="Areas Served Menu"
            class="absolute left-0 top-full pt-2 w-64 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform origin-top-left z-50 list-none m-0 p-0">
            <li role="none"
              class="bg-white shadow-xl rounded-lg border border-slate-100 overflow-hidden flex flex-col max-h-96 overflow-y-auto">
              <a href="/areas-served/houston/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Houston</a>
              <a href="/areas-served/pasadena/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Pasadena</a>
              <a href="/areas-served/baytown/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Baytown</a>
              <a href="/areas-served/deer-park/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Deer
                Park</a>
              <a href="/areas-served/la-porte/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">La
                Porte</a>
              <a href="/areas-served/league-city/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">League
                City</a>
              <a href="/areas-served/pearland/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Pearland</a>
              <a href="/areas-served/friendswood/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Friendswood</a>
              <a href="/areas-served/clear-lake/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Clear
                Lake</a>
              <a href="/areas-served/seabrook/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Seabrook</a>
              <a href="/areas-served/kemah/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Kemah</a>
              <a href="/areas-served/texas-city/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Texas
                City</a>
              <a href="/areas-served/galveston/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Galveston</a>
              <a href="/areas-served/alvin/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Alvin</a>
              <a href="/areas-served/missouri-city/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Missouri
                City</a>
              <a href="/areas-served/sugar-land/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Sugar
                Land</a>
              <a href="/areas-served/katy/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Katy</a>
              <a href="/areas-served/cypress/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Cypress</a>
              <a href="/areas-served/spring/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Spring</a>
              <a href="/areas-served/the-woodlands/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">The
                Woodlands</a>
              <a href="/areas-served/conroe/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Conroe</a>
              <a href="/areas-served/webster/" role="menuitem"
                class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Webster</a>
            </li>
          </ul>
        </li>

        <li role="none">
          <a href="/general-construction/" role="menuitem"
            class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">General
            Construction</a>
        </li>
        <li role="none">
          <a href="/faq/" role="menuitem"
            class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">FAQ</a>
        </li>
        <li role="none">
          <a href="/project-gallery/" role="menuitem"
            class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">Gallery</a>
        </li>
        <li role="none">
          <a href="/contact-us/" role="menuitem"
            class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">Contact</a>
        </li>
      </ul>'''

# Get all area pages
area_dirs = [d for d in os.listdir('areas-served') if os.path.isdir(os.path.join('areas-served', d))]

fixed_count = 0

for city in area_dirs:
    file_path = f'areas-served/{city}/index.html'
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the desktop menu section
    # Pattern: from opening tag with desktop-menu id to the closing tag before "Get Estimate" button
    pattern = r'<(?:div|ul) class="hidden lg:flex[^"]*" id="desktop-menu"[^>]*>.*?</(?:div|ul)>\s*<div class="hidden lg:block">'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        old_menu = match.group(0)
        # Replace but keep the final closing tag for the button container
        new_menu = semantic_nav + '\n      <div class="hidden lg:block">'
        new_content = content.replace(old_menu, new_menu)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        fixed_count += 1
        print(f"✅ Updated {city} with semantic navigation")
    else:
        print(f"⚠️  Could not find menu pattern in {city}")

print(f"\n✅ Updated {fixed_count} area pages with semantic navigation")
print(f"📋 Added semantic <ul>/<li> structure")
print(f"♿ Added WAI-ARIA attributes (role, aria-haspopup, aria-expanded)")
print(f"🤖 All 22 city links hard-coded for search bot crawlability")
print(f"🎨 Preserved all CSS classes for consistent styling")
