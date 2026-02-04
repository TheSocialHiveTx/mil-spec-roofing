import os

# Root Dir
root_dir = os.getcwd()

# Template for the Service Page
# We will use string formatting for Title, Description, Content
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Mil-Spec Roofing Services</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://mil-specroofing.com/services/{slug}/">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/style.css">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-slate-50 font-sans text-slate-900">

    <!-- Navbar -->
    <nav id="navbar" class="fixed w-full z-50 transition-all duration-300 bg-white/90 backdrop-blur-sm py-4">
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
                    <div class="absolute left-0 top-full pt-2 w-64 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 transform origin-top-left z-50">
                        <div class="bg-white shadow-xl rounded-lg border border-slate-100 overflow-hidden flex flex-col">
                            <a href="/services/residential-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Residential Roofing</a>
                            <a href="/services/commercial-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Commercial Roofing</a>
                             <a href="/services/roof-repair/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof Repair</a>
                            <a href="/services/roof-replacement/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Roof Replacement</a>
                            <a href="/services/emergency-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Emergency Roofing</a>
                            <a href="/services/" class="block px-4 py-3 text-xs font-bold uppercase text-blue-600 bg-slate-50 hover:bg-slate-100 text-center">View All Services</a>
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
                            <a href="/areas-served/the-woodlands/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">The Woodlands</a>
                            <a href="/areas-served/katy/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Katy</a>
                            <a href="/areas-served/sugar-land/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Sugar Land</a>
                            <a href="/areas-served/pearland/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Pearland</a>
                            <a href="/areas-served/league-city/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">League City</a>
                             <a href="/areas-served/pasadena/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Pasadena</a>
                             <a href="/areas-served/conroe/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Conroe</a>
                             <a href="/areas-served/galveston/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Galveston</a>
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
    </nav>

    <!-- Hero -->
    <section class="relative py-24 bg-slate-900 flex flex-col items-center justify-center text-center px-4 overflow-hidden">
        <div class="absolute top-0 right-0 w-64 h-64 bg-blue-600/10 rounded-full blur-3xl -mr-32 -mt-32"></div>
        <div class="absolute bottom-0 left-0 w-64 h-64 bg-blue-600/10 rounded-full blur-3xl -ml-32 -mb-32"></div>
         <div class="relative z-10 max-w-3xl pt-16">
            <div class="inline-flex items-center space-x-2 bg-blue-600/20 border border-blue-500/30 rounded-full px-4 py-1 mb-6 backdrop-blur-sm">
                <span class="text-blue-200 text-xs font-bold uppercase tracking-widest">Mil-Spec Standard</span>
            </div>
            <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-6">
                {title}
            </h1>
            <p class="text-lg text-slate-300">{short_desc}</p>
        </div>
    </section>

    <!-- Main Content -->
    <section class="py-20 bg-white">
        <div class="container mx-auto px-4">
            <div class="flex flex-col lg:flex-row gap-12">
                <!-- Left: Content -->
                <div class="lg:w-2/3">
                    <h2 class="text-3xl font-bold text-slate-900 mb-6">Service Overview</h2>
                    <p class="text-lg text-slate-600 leading-relaxed mb-8">
                        {long_desc}
                    </p>

                    <h3 class="text-2xl font-bold text-slate-900 mb-4">Key Benefits</h3>
                    <ul class="space-y-4 mb-12">
                        {benefits_html}
                    </ul>

                    <div class="bg-blue-50 border border-blue-100 p-8 rounded-lg">
                        <h4 class="text-xl font-bold text-slate-900 mb-2">Why Choose Mil-Spec?</h4>
                        <p class="text-slate-600 mb-6">We bring military discipline to every job site. No shortcuts, clean worksites, and clear communication.</p>
                        <a href="/contact-us/" class="inline-block bg-blue-600 text-white px-8 py-3 rounded-sm font-bold uppercase tracking-wider hover:bg-blue-700 transition-colors">Request Inspection</a>
                    </div>
                </div>

                <!-- Right: Sidebar -->
                <div class="lg:w-1/3">
                    <div class="bg-slate-50 p-6 rounded-lg border border-slate-100 sticky top-24">
                        <h4 class="font-bold text-slate-900 uppercase tracking-wider mb-4 border-b pb-2">All Services</h4>
                        <ul class="space-y-2 text-sm">
                            <li><a href="/services/residential-roofing/" class="block py-2 text-slate-600 hover:text-blue-600 hover:pl-2 transition-all border-b border-slate-100">Residential Roofing</a></li>
                            <li><a href="/services/commercial-roofing/" class="block py-2 text-slate-600 hover:text-blue-600 hover:pl-2 transition-all border-b border-slate-100">Commercial Roofing</a></li>
                            <li><a href="/services/roof-repair/" class="block py-2 text-slate-600 hover:text-blue-600 hover:pl-2 transition-all border-b border-slate-100">Roof Repair</a></li>
                            <li><a href="/services/roof-replacement/" class="block py-2 text-slate-600 hover:text-blue-600 hover:pl-2 transition-all border-b border-slate-100">Roof Replacement</a></li>
                            <li><a href="/services/roof-inspection/" class="block py-2 text-slate-600 hover:text-blue-600 hover:pl-2 transition-all border-b border-slate-100">Roof Inspection</a></li>
                            <li><a href="/services/emergency-roofing/" class="block py-2 text-slate-600 hover:text-blue-600 hover:pl-2 transition-all border-b border-slate-100">Emergency Roofing</a></li>
                        </ul>
                        <div class="mt-8">
                            <h4 class="font-bold text-slate-900 uppercase tracking-wider mb-4">Contact</h4>
                            <p class="text-slate-600 mb-2"><i data-lucide="phone" class="inline w-4 h-4 mr-2"></i> 281-813-5925</p>
                            <p class="text-slate-600"><i data-lucide="map-pin" class="inline w-4 h-4 mr-2"></i> Houston, TX</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer Script -->
    <script src="/script.js" defer></script>
</body>
</html>
"""

# Data Source (Reconstructed & Enhanced)
service_data = {
    'residential-roofing': {
        'title': 'Residential Roofing',
        'short_desc': 'Protecting your home with military-grade precision and premium materials.',
        'meta_desc': 'Expert residential roofing services in Houston. Asphalt, metal, and tile roofing installed with integrity and a workmanship guarantee.',
        'long_desc': 'Your home is your sanctuary, and the roof is its first line of defense. We specialize in high-performance residential roofing systems that blend aesthetic appeal with precision installation. Whether you prefer architectural shingles, impact-resistant synthetic slate, or standing seam metal, our installation process is rigorous, documented, and backed by a workmanship guarantee.',
        'benefits': ['Lifetime Manufacturer Warranties', 'Class 4 Impact Resistance Options', 'Enhanced Ventilation Systems', 'Daily Site Cleanup & Safety Checks']
    },
    'commercial-roofing': {
        'title': 'Commercial Roofing',
        'short_desc': 'Durable, energy-efficient roofing systems for businesses and industrial facilities.',
        'meta_desc': 'Commercial roofing contractors in Houston. TPO, EPDM, and flat roof coatings for businesses, warehouses, and office complexes.',
        'long_desc': 'Business continuity relies on a secure facility. Our commercial division handles everything from flat roof restorations to complex new construction projects. We work with TPO, EPDM, PVC, and Modified Bitumen systems, ensuring your business stays dry and energy-efficient. We plan our work to minimize disruption to your daily operations.',
        'benefits': ['Energy-Star Rated Materials', 'NDL (No Dollar Limit) Warranties', 'Preventative Maintenance Plans', 'Leak-Free Guarantee']
    },
    'roof-repair': {
        'title': 'Roof Repair',
        'short_desc': 'Fast, effective repairs to stop leaks and extend the life of your roof.',
        'meta_desc': 'Emergency roof repair in Houston. Fix leaks, missing shingles, and storm damage fast with Mil-Spec Roofing.',
        'long_desc': 'Not every roof needs replacement. Mil-Spec Roofing provides honest, targeted repairs for leaks, flashing failures, and storm damage. We identify the root cause of the issue—not just the symptom—and implement a lasting fix. We won\'t upsell you a new roof if a repair is the right mission choice.',
        'benefits': ['Comprehensive Leak Detection', 'Color-Matched Shingle Replacement', 'Flashing & Boot Resealing', 'Detailed Before/After Photos']
    },
    'roof-replacement': {
        'title': 'Roof Replacement',
        'short_desc': 'Complete roof system replacement with superior materials and craftsmanship.',
        'meta_desc': 'Full roof replacement services. Upgrade your home protection with a new roof installed by veterans.',
        'long_desc': 'When a roof reaches the end of its service life, a full replacement is an investment in your property\'s future value and safety. We strip the roof to the deck, inspect for structural rot, improve ventilation, and install a complete roofing system—not just new shingles. Our crews are trained to install to manufacturer specifications to ensure full warranty coverage.',
        'benefits': ['Full Deck Inspection', 'Ice & Water Shield Upgrade', 'High-Wind Rated Shingles', '10-Year Workmanship Warranty']
    },
    'roof-installation': {
        'title': 'New Roof Installation',
        'short_desc': 'Precision roof construction for new homes and additions.',
        'meta_desc': 'New construction roofing experts. We work with builders and homeowners to install the perfect roof from day one.',
        'long_desc': 'Building a new home or addition requires coordination and precision. We work directly with builders and homeowners to select the best roofing materials for the structure and budget. Our new installation process focuses on proper decking, calculating optimal net-free ventilation, and flashing details that are often overlooked by volume builders.',
        'benefits': ['Blueprint Estimation', 'Builder Coordination', 'Custom Flashing Fabrication', 'Final Inspection Report']
    },
    'roof-inspection': {
        'title': 'Roof Inspection',
        'short_desc': 'Detailed assessments to verify condition and identify risks.',
        'meta_desc': 'Professional roof inspections in Houston. Get a detailed report on your roof\'s condition for insurance or real estate.',
        'long_desc': 'Knowledge is power. Our multi-point roof inspections provide a clear, unbiased assessment of your roof\'s condition. Whether you are buying a home, filing an insurance claim, or just planning for maintenance, our detailed reports (complete with photos) give you the intel you need to make the right decision.',
        'benefits': ['Drone Inspection Capable', 'Hail & Wind Damage Assessment', 'Real Estate Certifications', 'Est. Remaining Life Analysis']
    },
    'emergency-roofing': {
        'title': 'Emergency Roofing',
        'short_desc': '24/7 Rapid response for severe storm damage and active leaks.',
        'meta_desc': 'Emergency roofing services. We deploy fast to stop leaks and stabilize your home after severe weather.',
        'long_desc': 'When the weather hits hard, Mil-Spec hits back. Our emergency response teams are ready to deploy when you have major structural damage or active water intrusion. We focus on immediate stabilization—stopping the water, removing debris, and securing the property—so you can sleep safely while permanent repairs are planned.',
        'benefits': ['Rapid Response Teams', 'Tree Removal Coordination', 'Temporary Dry-In', 'Insurance Documentation']
    },
    'roof-tarping': {
        'title': 'Roof Tarping',
        'short_desc': 'Professional tarp installation to prevent water damage.',
        'meta_desc': 'Emergency roof tarping. heavy-duty tarps installed correctly to protect your home until repairs can be made.',
        'long_desc': 'A blue tarp is your home\'s temporary shield. But a poorly installed tarp usually fails in the next wind gust. We install professional-grade, secured tarps using proper battens and attachment methods. This prevents further interior water damage and shows the insurance company you took mitigating action.',
        'benefits': ['Heavy-Duty Reinforced Tarps', 'Secure Batten Installation', 'Up to 90 Days Protection', 'Prevents Mold Growth']
    },
    'flat-roofing': {
         'title': 'Flat Roofing',
         'short_desc': 'Specialized solutions for low-slope and flat residential/commercial roofs.',
         'meta_desc': 'Flat roof experts. TPO, Modified Bitumen, and coatings for modern homes and businesses.',
         'long_desc': 'Flat roofs face unique challenges, primarily drainage and UV degradation. Standard shingles won\'t work here. We install specialized low-slope systems like self-adhering modified bitumen for residential lanais/porches, or TPO membranes for larger commercial decks. Proper taper systems and crickets are installed to ensure positive drainage.',
         'benefits': ['Ponding Water Solutions', 'Reflective Cool Roof Options', 'Seamless Membrane Systems', 'Scupper & Drain Upgrades']
    },
    'multi-family-roofing': {
         'title': 'Multi-Family Roofing',
         'short_desc': 'Large-scale roofing for apartments, condos, and HOAs.',
         'meta_desc': 'Multi-family roofing contractors. Capable of handling large apartment complexes and HOA replacement projects.',
         'long_desc': 'Managing a roofing project for an apartment complex or HOA requires logistics, speed, and safety. We scale our workforce to handle multiple buildings simultaneously, minimizing inconvenience to tenants. We provide clear communication to property managers and maintain a clean, nail-free ground environment daily.',
         'benefits': ['Tenant Notification Plans', 'Phased Installation Scheduling', 'Uniformity & HOA Compliance', 'Volume Pricing']
    },
    'gutters-siding': {
         'title': 'Gutters & Siding',
         'short_desc': 'Complete exterior protection: Seamless gutters and Hardie siding.',
         'meta_desc': 'Gutters and siding installation. Protect your siding and foundation with properly sized seamless gutters.',
         'long_desc': 'Water management is critical. A good roof needs good gutters to move water away from your foundation. We install 5" and 6" seamless aluminum gutters in various colors. We also repair and replace siding, typically using James Hardie fiber cement products for superior durability against Texas heat and rot.',
         'benefits': ['Seamless Aluminum Gutters', 'Leaf Guard Protection', 'Fiber Cement Siding', 'Soffit & Fascia Repair']
    },
    'insurance-claims': {
         'title': 'Insurance Claims Support',
         'short_desc': 'We advocate for you during the insurance process.',
         'meta_desc': 'Roof insurance claim help. We simplify the claims process and ensure you get fair coverage for storm damage.',
         'long_desc': 'Dealing with insurance adjusters can be confusing. We speak their language (Xactimate). While we are not public adjusters, we provide the technical expertise and documentation needed to justify your claim. We meet the adjuster on the roof to ensure they see every hail hit and wind-creased shingle.',
         'benefits': ['Adjuster Meet-and-Greets', 'Xactimate Estimates', 'Code Upgrade Verification', 'Supplement Filing']
    }
}

for slug, data in service_data.items():
    # Construct paths
    dir_path = os.path.join(root_dir, 'services', slug)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, 'index.html')
    
    # Generate Benefits HTML
    benefits_list = data['benefits']
    benefits_html = ""
    for b in benefits_list:
        benefits_html += f'<li class="flex items-center text-slate-700"><i data-lucide="check-circle" class="w-5 h-5 text-blue-600 mr-3"></i> {b}</li>'
    
    # Format Template
    page_content = html_template.format(
        slug=slug,
        title=data['title'],
        short_desc=data['short_desc'],
        meta_desc=data['meta_desc'],
        long_desc=data['long_desc'],
        benefits_html=benefits_html
    )
    
    # Write File
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(page_content)
    
    print(f"Generated Content for: {slug} -> {file_path}")

print("All Service Pages Regenerated Successfully.")
