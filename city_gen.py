import os
import random

root_dir = os.getcwd()
template_path = os.path.join(root_dir, "services", "index.html")

cities = [
    "Houston", "Pasadena", "Baytown", "Deer Park", "La Porte", "League City",
    "Pearland", "Friendswood", "Clear Lake", "Seabrook", "Kemah", "Texas City",
    "Galveston", "Alvin", "Missouri City", "Sugar Land", "Katy", "Cypress",
    "Spring", "The Woodlands", "Conroe", "Webster"
]

# SEO Content Generators
CITY_INTRO_COPY = {
    "Houston": "In <strong>Houston</strong>, roofs have to handle intense heat, sudden storms, and year-round exposure. We focus on resilient assemblies with tight flashing, proper ventilation, and material options that prioritize long-term performance. From large commercial sites to residential neighborhoods, our team delivers disciplined workmanship and clear communication.",
    "Pasadena": "Homeowners and businesses in <strong>Pasadena</strong> need roofing that holds up under heavy rain and wind-driven debris. We prioritize leak prevention, clean water flow, and detail-focused installation to reduce future maintenance. If you are facing storm damage or an aging roof, we provide direct guidance and dependable fixes.",
    "Baytown": "In <strong>Baytown</strong>, a roof has to stand up to humid weather and fast-changing storms. Our crews pay special attention to underlayment, flashing, and seal integrity so water stays out and performance stays consistent. We help you select materials that balance durability, budget, and curb appeal.",
    "Deer Park": "Roofing in <strong>Deer Park</strong> calls for careful workmanship and a clean jobsite from start to finish. We run thorough inspections, document issues, and repair the weak points before they become expensive problems. When replacement is needed, we build systems designed for longevity and smooth drainage.",
    "La Porte": "For <strong>La Porte</strong> properties, moisture control and wind resistance are key. We reinforce vulnerable transitions, upgrade flashing where it matters, and ensure your roof sheds water efficiently. The result is a tighter, tougher roof that stands up to local conditions.",
    "League City": "In <strong>League City</strong>, homeowners often want a roof that performs well and looks sharp. We guide you through material choices, color options, and system upgrades that improve both protection and curb appeal. Our process stays clear, organized, and on schedule.",
    "Pearland": "In <strong>Pearland</strong>, we help property owners protect their investment with roofing built for efficiency and durability. We evaluate ventilation, decking condition, and drainage so the whole system works together. Whether you need repair or replacement, our approach is methodical and transparent.",
    "Friendswood": "Residents in <strong>Friendswood</strong> expect craftsmanship that respects their home and property. We use careful staging, protect landscaping, and keep communication tight throughout the project. The end result is a clean install, a reliable roof, and a crew you can trust.",
    "Clear Lake": "In <strong>Clear Lake</strong>, humidity and rain put extra stress on roofing systems. We focus on moisture control, algae-resistant material options, and gutters that move water away fast. The goal is a roof that stays dry, clean, and durable.",
    "Seabrook": "For <strong>Seabrook</strong> roofs, wind and moisture are constant factors. We use proven fastening patterns, upgraded sealants, and edge details that help prevent lift and leaks. It is a straightforward approach built for consistent protection.",
    "Kemah": "In <strong>Kemah</strong>, coastal air can be tough on exterior materials. We recommend corrosion-resistant components and install with extra attention to seams, flashings, and penetrations. That added precision helps your roof hold up longer with fewer surprises.",
    "Texas City": "Homeowners and businesses in <strong>Texas City</strong> need fast, reliable help after severe weather. We offer responsive inspections, temporary protection when needed, and permanent repairs that restore full performance. You will get clear documentation and a plan you can trust.",
    "Galveston": "In <strong>Galveston</strong>, roofs must be ready for strong coastal winds and storm season. We build high-integrity systems with secure fastening, reinforced edges, and materials chosen for toughness. Our team helps you prepare, repair, or replace with confidence.",
    "Alvin": "In <strong>Alvin</strong>, temperature swings and hail can take a toll on shingles and flashing. We install impact-aware options, verify attic airflow, and reinforce vulnerable roof zones. The result is better protection and fewer surprises down the road.",
    "Missouri City": "For <strong>Missouri City</strong> properties, we deliver roofing solutions that balance performance and value. From precise repairs to full replacements, our crew focuses on system integrity, clean lines, and long-term reliability. We keep the process simple and transparent.",
    "Sugar Land": "Homeowners in <strong>Sugar Land</strong> often want a roof that complements the home while delivering top-tier protection. We walk you through premium materials, refined details, and upgrades that add lasting value. Every install is clean, intentional, and built to last.",
    "Katy": "In <strong>Katy</strong>, growth means a mix of newer builds and aging roofs. We provide tailored inspections, smart repair options, and complete replacements built for durability. Our team keeps timelines tight and communication clear.",
    "Cypress": "For <strong>Cypress</strong> properties, debris, heavy rain, and heat can add up fast. We focus on strong water barriers, clean drainage, and detail-driven installs that resist wear. It is a practical approach that keeps roofs dependable year after year.",
    "Spring": "In <strong>Spring</strong>, many homes need straightforward, honest roofing guidance. We document what we find, prioritize critical fixes, and explain your options without pressure. Whether it is a repair or replacement, we deliver disciplined workmanship you can count on.",
    "The Woodlands": "Roofs in <strong>The Woodlands</strong> face shade, moisture, and occasional storm debris. We address ventilation, flashing, and drainage so the system performs as designed. That attention to detail helps prevent hidden leaks and early wear.",
    "Conroe": "In <strong>Conroe</strong>, we help property owners protect their homes with roofing designed for durability and clean water flow. Our process starts with a detailed inspection and ends with a system built to last. You will always know what we are doing and why.",
    "Webster": "As a local team serving <strong>Webster</strong>, we can respond quickly and keep the process personal. We focus on clear communication, precise repairs, and clean installations that hold up to Texas weather. When you need help, we are nearby and ready."
}

CITY_MAP_COPY = {
    "Houston": "We are set up to respond quickly across Houston with crews ready for inspections, repairs, or full replacements.",
    "Pasadena": "Local crews can be on-site in Pasadena quickly to assess damage and plan the right fix.",
    "Baytown": "We serve Baytown with responsive inspections and a straightforward plan for repairs or replacement.",
    "Deer Park": "Our team provides fast, reliable roofing support throughout Deer Park and nearby neighborhoods.",
    "La Porte": "We are positioned to serve La Porte with timely inspections and durable roofing solutions.",
    "League City": "League City homeowners can expect prompt scheduling and a clean, efficient install process.",
    "Pearland": "We respond across Pearland with clear estimates and roofing built for long-term performance.",
    "Friendswood": "Friendswood residents get disciplined workmanship, quick response times, and careful jobsite practices.",
    "Clear Lake": "Clear Lake properties receive fast assessments and moisture-focused roofing solutions.",
    "Seabrook": "Seabrook homeowners can count on responsive service and detail-focused roofing work.",
    "Kemah": "We serve Kemah with coastal-ready materials and fast, reliable scheduling.",
    "Texas City": "Texas City clients get quick inspections, temporary protection when needed, and lasting repairs.",
    "Galveston": "We are ready to help Galveston with storm-ready roofing and fast response times.",
    "Alvin": "Alvin homeowners can expect efficient inspections and durable, impact-aware roofing options.",
    "Missouri City": "We support Missouri City with clear scopes of work and dependable roofing systems.",
    "Sugar Land": "Sugar Land residents receive premium materials, tight detailing, and clean installs.",
    "Katy": "Katy clients get fast scheduling and roofing tailored to their home needs.",
    "Cypress": "We serve Cypress with reliable inspections and water-tight roofing systems.",
    "Spring": "Spring homeowners can count on honest assessments and disciplined workmanship.",
    "The Woodlands": "We help The Woodlands with moisture-aware roofing and careful system detailing.",
    "Conroe": "Conroe properties receive clear, step-by-step roofing guidance and durable installs.",
    "Webster": "Webster residents get local, fast response and a team that knows the area."
}


def get_intro_text(city):
    return CITY_INTRO_COPY.get(
        city,
        f"Mil-Spec Roofing provides full-service roofing solutions for residential and commercial properties in {city}."
    )


def get_meta_desc(city):
    return (
        f"Trusted roofing contractor in {city}, TX. Veteran-owned, faith-based experts in storm repair, "
        f"roof replacement, and commercial roofing. Get a free inspection in {city} today."
    )


with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

for city in cities:
    city_slug = city.lower().replace(" ", "-")
    dir_path = os.path.join(root_dir, "areas-served", city_slug)
    os.makedirs(dir_path, exist_ok=True)

    # Customization
    content = template

    # 1. Title Tag
    content = content.replace(
        "<title>Roofing Services | Mil-Spec Roofing & Construction Houston TX</title>",
        f"<title>Roofing Services in {city}, TX | Mil-Spec Roofing</title>"
    )

    # 2. Meta Description
    # We use a regex or specific target string replacement if we can identify it,
    # but the template has a specific generic one we can target.
    content = content.replace(
        'content="Veteran-owned, faith-based roofing services in Houston and Southeast Texas.',
        f'content="{get_meta_desc(city)}'
    )

    # 3. H2 Heading (Main Service Header)
    content = content.replace(
        'Roofing <span class="text-blue-600">Services in Texas</span>',
        f'Roofing <span class="text-blue-600">Services in {city}</span>'
    )

    # 4. Intro Paragraph (The big SEO win)
    rich_text = get_intro_text(city)
    intro_open = '<p class="text-slate-600 max-w-2xl mx-auto text-lg">'
    intro_close = "</p>"
    intro_start = content.find(intro_open)
    if intro_start != -1:
        intro_end = content.find(intro_close, intro_start)
        if intro_end != -1:
            before = content[:intro_start + len(intro_open)]
            after = content[intro_end:]
            content = (
                before
                + "\n            "
                + rich_text
                + "\n          "
                + after
            )

    # 5. Service Cards (Localizing the links/text slightly? No, keep generic services but maybe add "in {city}" to alt tags?)
    content = content.replace(
        '<h3 class="text-2xl font-extrabold text-slate-900 mb-3 uppercase tracking-tight">Who We Are</h3>',
        f'<h3 class="text-2xl font-extrabold text-slate-900 mb-3 uppercase tracking-tight">Serving {city} with Honor</h3>'
    )

    # 6. Hero H1 - Make it LOCAL
    # Target: Mission-Ready <span class="text-blue-500">Roofing Services</span>
    content = content.replace(
        'Mission-Ready <span class="text-blue-500">Roofing Services</span>',
        f'Roofing Services <span class="text-blue-500">in {city}</span>'
    )

    # 7. Canonical Tag & Schema
    # Canonical: <link rel="canonical" href="https://mil-specroofing.com/services" />
    content = content.replace(
        '<link rel="canonical" href="https://mil-specroofing.com/services" />',
        f'<link rel="canonical" href="https://mil-specroofing.com/areas-served/{city_slug}/" />'
    )

    # Schema ID/URL
    content = content.replace(
        '"url": "https://mil-specroofing.com/services"',
        f'"url": "https://mil-specroofing.com/areas-served/{city_slug}/"'
    )
    content = content.replace(
        '"name": "Roofing Services | Mil-Spec Roofing"',
        f'"name": "Roofing Services in {city} | Mil-Spec Roofing"'
    )
    content = content.replace(
        '@id": "https://mil-specroofing.com/services#webpage"',
        f'@id": "https://mil-specroofing.com/areas-served/{city_slug}/#webpage"'
    )

    # 8. City Specific Map
    # The template (services/index.html) does NOT have a map. We must inject it.
    # We will insert it before the final CTA section.
    cta_marker = '<section class="py-16 bg-blue-600 text-white text-center">'

    map_html = f"""
    <section class="py-20 bg-white">
        <div class="container mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
                    Serving <span class="text-blue-600">{city}</span> & Surrounding Areas
                </h2>
                <div class="h-1 w-20 bg-blue-600 mx-auto rounded-full mb-6"></div>
                <p class="text-slate-600 max-w-2xl mx-auto">
                    {CITY_MAP_COPY.get(city, f"We are locally positioned to respond rapidly to any roofing needs in {city}.")}
                </p>
            </div>
            <div class="w-full h-96 bg-slate-100 rounded-2xl overflow-hidden shadow-lg border border-slate-200">
                <iframe
                    src="https://maps.google.com/maps?width=100%25&height=600&hl=en&q={city}%20TX&t=&z=13&ie=UTF8&iwloc=B&output=embed"
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

    if cta_marker in content:
        content = content.replace(cta_marker, map_html + "\n" + cta_marker)
    else:
        print(f"Warning: Could not find CTA marker in {city}")

    # 9. Remove the "Serving All of Southeast Texas" Regional Map
    # Depending on how it's formatted in the template, we will try to target the block carefully.
    # It starts with <!-- Regional Map --> and ends with </section> before the footer.
    # We can try a regex or a simple find.
    start_marker = "<!-- Regional Map -->"
    end_marker = '<footer class="bg-slate-950'

    if start_marker in content and end_marker in content:
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)
        if start_idx != -1 and end_idx != -1:
            # Removing clearly from start of comment to start of footer
            content = content[:start_idx] + content[end_idx:]
    else:
        # Fallback if precise markers fail (e.g. whitespace issues), try removing by header
        section_header = 'Serving All of <span class="text-blue-600">Southeast Texas</span>'
        if section_header in content:
            # This is riskier without clear bounds, but lets try to remove the section context
            pass

    # Write
    dest_path = os.path.join(dir_path, "index.html")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated SEO Optimized Page for {city}")
