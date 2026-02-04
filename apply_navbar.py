import os
import re

root_dir = os.getcwd()

# The NEW Navbar HTML with Comprehensive Services Dropdown
new_navbar = """<nav id="navbar" class="fixed w-full z-50 transition-all duration-300 bg-white/90 backdrop-blur-sm py-4">
        <div class="container mx-auto px-4 flex justify-between items-center">
            <a href="/" class="flex items-center cursor-pointer group">
                <div class="flex flex-col items-center">
                    <img src="/images/mil-spec roofing logo.png" alt="Mil-Spec Roofing Logo" class="h-12 w-auto">
                </div>
            </a>
            <div class="hidden lg:flex space-x-6 items-center" id="desktop-menu">
                <a href="/" class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">Home</a>
                
                <!-- Services Dropdown -->
                <div class="relative group">
                    <a href="/services/" class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500 flex items-center gap-1 py-4">
                        Services <i data-lucide="chevron-down" class="h-4 w-4"></i>
                    </a>
                    <div class="absolute left-0 top-full pt-2 w-72 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform origin-top-left z-50">
                        <div class="bg-white shadow-xl rounded-lg border border-slate-100 overflow-hidden flex flex-col max-h-[80vh] overflow-y-auto">
                            <a href="/services/residential-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Residential Roofing</a>
                            <a href="/services/commercial-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Commercial Roofing</a>
                            <a href="/services/roof-repair/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof Repair</a>
                            <a href="/services/roof-replacement/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof Replacement</a>
                            <a href="/services/roof-installation/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof Installation</a>
                            <a href="/services/flat-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Flat Roofing</a>
                            <a href="/services/multi-family-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Multi-Family Roofing</a>
                            <a href="/services/metal-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Metal Roofing</a>
                            <a href="/services/emergency-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Emergency Roofing</a>
                            <a href="/services/roof-tarping/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof Tarping</a>
                            <a href="/services/roof-inspection/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof Inspection</a>
                            <a href="/services/gutters-siding/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Gutters & Siding</a>
                            <a href="/services/insurance-claims/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Insurance Claims</a>
                            <a href="/services/" class="block px-4 py-3 text-xs font-bold uppercase text-blue-600 bg-slate-50 hover:bg-slate-100 text-center sticky bottom-0">View All Services</a>
                        </div>
                    </div>
                </div>

                <!-- Areas Served Dropdown -->
                <div class="relative group">
                     <a href="#" class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500 flex items-center gap-1 py-4">
                        Areas Served <i data-lucide="chevron-down" class="h-4 w-4"></i>
                    </a>
                    <div class="absolute left-0 top-full pt-2 w-64 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform origin-top-left z-50">
                        <div class="bg-white shadow-xl rounded-lg border border-slate-100 overflow-hidden flex flex-col max-h-96 overflow-y-auto">
                            <a href="/areas-served/houston/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Houston</a>
                            <a href="/areas-served/pasadena/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Pasadena</a>
                            <a href="/areas-served/baytown/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Baytown</a>
                            <a href="/areas-served/deer-park/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Deer Park</a>
                            <a href="/areas-served/la-porte/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">La Porte</a>
                            <a href="/areas-served/league-city/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">League City</a>
                            <a href="/areas-served/pearland/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Pearland</a>
                            <a href="/areas-served/friendswood/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Friendswood</a>
                            <a href="/areas-served/clear-lake/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Clear Lake</a>
                            <a href="/areas-served/seabrook/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Seabrook</a>
                            <a href="/areas-served/kemah/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Kemah</a>
                            <a href="/areas-served/texas-city/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Texas City</a>
                            <a href="/areas-served/galveston/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Galveston</a>
                            <a href="/areas-served/alvin/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Alvin</a>
                            <a href="/areas-served/missouri-city/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Missouri City</a>
                            <a href="/areas-served/sugar-land/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Sugar Land</a>
                            <a href="/areas-served/katy/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Katy</a>
                            <a href="/areas-served/cypress/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Cypress</a>
                            <a href="/areas-served/spring/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Spring</a>
                            <a href="/areas-served/the-woodlands/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">The Woodlands</a>
                            <a href="/areas-served/conroe/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Conroe</a>
                            <a href="/areas-served/webster/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Webster</a>
                        </div>
                    </div>
                </div>

                <a href="/general-construction/" class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">General Construction</a>
                <a href="/faq/" class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">FAQ</a>
                <a href="/about-us/" class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">About</a>
                <a href="/project-gallery/" class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">Gallery</a>
                <a href="/contact-us/" class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">Contact</a>
            </div>
            <div class="hidden lg:block">
                 <a href="/contact-us/" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2.5 rounded-sm font-bold uppercase text-xs tracking-wider shadow-md hover:shadow-lg transition-all transform hover:scale-105">Get Estimate</a>
            </div>
             <div class="lg:hidden">
                <button id="mobile-menu-btn" class="text-slate-800 focus:outline-none"><i data-lucide="menu" class="h-6 w-6"></i></button>
            </div>
        </div>
        <!-- Mobile Menu (Hidden by default, handled by script.js) -->
        <div id="mobile-menu" class="hidden lg:hidden bg-white absolute top-full left-0 w-full border-t border-slate-100 shadow-lg">
             <div class="flex flex-col p-4 space-y-4">
                <a href="/" class="mobile-nav-link text-sm font-bold uppercase text-slate-600">Home</a>
                <a href="/services/" class="mobile-nav-link text-sm font-bold uppercase text-blue-600">Services</a>
                <div class="pl-4 border-l-2 border-slate-100 space-y-2">
                    <a href="/services/residential-roofing/" class="block text-sm text-slate-500">Residential</a>
                    <a href="/services/commercial-roofing/" class="block text-sm text-slate-500">Commercial</a>
                    <a href="/services/roof-repair/" class="block text-sm text-slate-500">Repair</a>
                    <a href="/services/emergency-roofing/" class="block text-sm text-slate-500">Emergency</a>
                    <a href="/services/insurance-claims/" class="block text-sm text-slate-500">Insurance Claims</a>
                </div>
                 <div class="pl-4 border-l-2 border-slate-100 space-y-2">
                    <span class="block text-xs font-bold uppercase text-slate-400 mb-1">Areas</span>
                    <a href="/areas-served/houston/" class="block text-sm text-slate-500">Houston</a>
                    <a href="/areas-served/katy/" class="block text-sm text-slate-500">Katy</a>
                    <a href="/areas-served/the-woodlands/" class="block text-sm text-slate-500">The Woodlands</a>
                </div>
                <a href="/general-construction/" class="mobile-nav-link text-sm font-bold uppercase text-slate-600">General Construction</a>
                <a href="/contact-us/" class="bg-blue-600 text-white px-5 py-3 rounded-sm font-bold uppercase text-center w-full">Get Free Estimate</a>
             </div>
        </div>
    </nav>"""

# Match from <nav id="navbar" ... to </nav>
pattern = re.compile(r'<nav id="navbar".*?</nav>', re.DOTALL)

# Ignore these directories
ignore_dirs = {'.git', 'node_modules', '.gemini'}

for root, dirs, files in os.walk(root_dir):
    # Modify dirs in-place to skip ignored directories
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            
            # Skip if file is empty
            if os.path.getsize(file_path) == 0:
                continue

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if pattern.search(content):
                new_content = pattern.sub(new_navbar, content)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated Navbar in {file_path}")
            else:
                # Optional: Warn if navbar missing in an HTML file (might be a redirect file or snippet)
                pass
