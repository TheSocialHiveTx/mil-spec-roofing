import os
import re

# Service definitions with specific content
services = {
    'commercial-roofing': {
        'title': 'Commercial Roofing',
        'description': 'Protecting your business with military-grade commercial roofing systems.',
        'overview': 'Your commercial property demands roofing systems that can withstand heavy use, extreme weather, and the test of time. We specialize in TPO, EPDM, modified bitumen, and metal roofing systems designed for flat and low-slope applications. From office buildings to warehouses, our installations meet or exceed manufacturer specifications and local building codes.',
        'benefits': [
            'Energy-Efficient TPO & EPDM Systems',
            'Preventive Maintenance Programs',
            'Minimal Business Disruption',
            'OSHA-Compliant Job Sites'
        ]
    },
    'roof-repair': {
        'title': 'Roof Repair',
        'description': 'Fast, reliable roof repairs to protect your property.',
        'overview': 'Leaks, storm damage, and wear don\'t wait for convenient timing. Our roof repair services address issues quickly and thoroughly, whether it\'s a small penetration or significant wind damage. We diagnose the root cause, provide clear documentation, and execute repairs that restore your roof\'s integrity without unnecessary replacement.',
        'benefits': [
            'Same-Day Emergency Response Available',
            'Thermal Imaging Leak Detection',
            'Comprehensive Damage Documentation',
            '5-Year Workmanship Warranty on Repairs'
        ]
    },
    'roof-replacement': {
        'title': 'Roof Replacement',
        'description': 'Complete roof replacement systems built to last.',
        'overview': 'When repair isn\'t enough, we execute full roof replacement projects with military precision. Every replacement begins with a thorough deck inspection, includes proper ventilation upgrades, and follows strict manufacturer protocols. We use premium materials and provide lifetime warranties on materials plus extended workmanship guarantees.',
        'benefits': [
            'Lifetime Material Warranties Available',
            'Deck Inspection & Repair Included',
            'Enhanced Ventilation Systems',
            'Detailed Project Timeline & Updates'
        ]
    },
    'roof-installation': {
        'title': 'Roof Installation',
        'description': 'New construction and addition roofing installations.',
        'overview': 'Building new? We provide turnkey roof installation for new construction, additions, and detached structures. From structural decking to final shingle placement, we coordinate with your builder to ensure seamless integration, proper load calculations, and code-compliant ventilation. Every installation is backed by comprehensive warranties.',
        'benefits': [
            'Coordination with General Contractors',
            'Structural Load Analysis',
            'Code-Compliant Ventilation Design',
            'Manufacturer-Certified Installation'
        ]
    },
    'roof-inspection': {
        'title': 'Roof Inspection',
        'description': 'Professional roof inspections for buyers, sellers, and maintenance.',
        'overview': 'Knowledge is power. Our detailed roof inspections provide clear, photo-documented reports covering every aspect of your roof system. Whether you\'re buying, selling, filing an insurance claim, or planning preventive maintenance, our inspections give you the facts you need to make informed decisions.',
        'benefits': [
            'Thermal Imaging Technology',
            'Photo-Documented Reports',
            'Insurance Claim Support',
            'Maintenance Planning & Budgeting'
        ]
    },
    'emergency-roofing': {
        'title': 'Emergency Roofing',
        'description': '24/7 emergency roofing response for storm damage.',
        'overview': 'Storms don\'t wait for business hours. Our emergency roofing team responds rapidly to secure your property, prevent further damage, and begin the restoration process. From tarp installations to temporary repairs, we protect your property while developing a comprehensive permanent solution.',
        'benefits': [
            '24/7 Emergency Dispatch',
            'Rapid Tarp & Securing Services',
            'Insurance Documentation Support',
            'Expedited Permanent Repairs'
        ]
    },
    'flat-roofing': {
        'title': 'Flat Roofing',
        'description': 'Commercial and residential flat roofing systems.',
        'overview': 'Flat and low-slope roofs require specialized knowledge and materials. We install and repair TPO, EPDM, modified bitumen, and built-up roofing systems designed for commercial buildings, additions, and modern architectural homes. Proper drainage and flashing details are critical—we handle both expertly.',
        'benefits': [
            'TPO, EPDM & Modified Bitumen Systems',
            'Proper Drainage Design',
            'Energy-Efficient White Membranes',
            '20+ Year System Warranties'
        ]
    },
    'gutters-siding': {
        'title': 'Gutters & Siding',
        'description': 'Complete exterior protection systems.',
        'overview': 'Your roof is only as good as the systems supporting it. We install seamless gutters, downspouts, and siding that complement your roofing system while providing comprehensive weather protection. From gutter guards to impact-resistant siding, we ensure water management and exterior durability.',
        'benefits': [
            'Seamless Gutter Systems',
            'Gutter Guard Installation',
            'Impact-Resistant Siding Options',
            'Color-Matched to Roofing'
        ]
    },
    'insurance-claims': {
        'title': 'Insurance Claims',
        'description': 'Expert storm damage assessment and insurance claim support.',
        'overview': 'Navigating insurance claims can be overwhelming. We work directly with your insurance adjuster, provide detailed damage documentation, and ensure you receive fair compensation for storm damage. Our team understands what insurers require and presents claims that get approved.',
        'benefits': [
            'Free Insurance Inspections',
            'Detailed Damage Documentation',
            'Adjuster Meeting Support',
            'Supplemental Claim Assistance'
        ]
    },
    'multi-family-roofing': {
        'title': 'Multi-Family Roofing',
        'description': 'Roofing systems for apartments, condos, and multi-unit properties.',
        'overview': 'Multi-family properties present unique challenges: tenant coordination, HOA requirements, and budget constraints. We specialize in multi-building projects with phased scheduling, clear communication protocols, and systems designed for longevity. From garden-style apartments to high-rise condos, we deliver.',
        'benefits': [
            'Phased Project Scheduling',
            'Tenant Communication Protocols',
            'HOA Compliance Documentation',
            'Volume Pricing for Multiple Buildings'
        ]
    },
    'roof-tarping': {
        'title': 'Roof Tarping',
        'description': 'Emergency tarp services to prevent further damage.',
        'overview': 'When your roof is compromised, every hour counts. Our emergency tarping services secure your property quickly, preventing water intrusion and additional damage while we assess the situation and plan permanent repairs. We use commercial-grade materials and secure attachment methods.',
        'benefits': [
            'Emergency Response Available',
            'Commercial-Grade Tarps',
            'Secure Attachment Methods',
            'Insurance Documentation Included'
        ]
    }
}

# Read the residential roofing template
with open('services/residential-roofing/index.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Process each service
for service_slug, service_data in services.items():
    service_file = f'services/{service_slug}/index.html'
    
    if not os.path.exists(service_file):
        print(f"⚠️  Skipping {service_slug} - file not found")
        continue
    
    # Read current file to preserve JSON-LD
    with open(service_file, 'r', encoding='utf-8') as f:
        current_content = f.read()
    
    # Extract JSON-LD from current file
    json_ld_match = re.search(r'(<script type="application/ld\+json">.*?</script>)', current_content, re.DOTALL)
    if not json_ld_match:
        print(f"⚠️  No JSON-LD found in {service_slug}")
        continue
    
    json_ld = json_ld_match.group(1)
    
    # Get the HTML body part from template (everything after the first </script>)
    template_parts = template.split('</script>', 1)
    if len(template_parts) < 2:
        print(f"⚠️  Template structure issue")
        continue
    
    html_body = template_parts[1]
    
    # Customize the HTML body for this service
    html_body = html_body.replace('Residential Roofing', service_data['title'])
    html_body = html_body.replace('residential-roofing', service_slug)
    html_body = html_body.replace(
        'Protecting your home with military-grade precision and premium materials.',
        service_data['description']
    )
    html_body = html_body.replace(
        'Your home is your sanctuary, and the roof is its first line of defense. We specialize in high-performance residential roofing systems that blend aesthetic appeal with precision installation. Whether you prefer architectural shingles, impact-resistant synthetic slate, or standing seam metal, our installation process is rigorous, documented, and backed by a workmanship guarantee.',
        service_data['overview']
    )
    
    # Replace benefits list
    benefits_html = '\n                        '.join([
        f'<li class="flex items-center text-slate-700"><i data-lucide="check-circle" class="w-5 h-5 text-blue-600 mr-3"></i> {benefit}</li>'
        for benefit in service_data['benefits']
    ])
    
    # Find and replace the benefits section
    benefits_pattern = r'(<li class="flex items-center text-slate-700">.*?</li>\s*){4}'
    html_body = re.sub(benefits_pattern, benefits_html, html_body, count=1, flags=re.DOTALL)
    
    # Combine JSON-LD with customized HTML
    new_content = f"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n{json_ld}\n{html_body}"
    
    # Write the new file
    with open(service_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Built complete page for {service_slug}")

print(f"\n✅ All service pages now have full HTML content matching residential-roofing template")
