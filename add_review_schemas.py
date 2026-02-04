import os
import json
import re

# Real Google reviews data
reviews = [
    {
        "@type": "Review",
        "author": {
            "@type": "Person",
            "name": "Matthew Carraway"
        },
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": "5",
            "bestRating": "5"
        },
        "datePublished": "2023-03-16",
        "reviewBody": "This company is great to deal with. No pressure and honest. I knew I needed a repair or new roof resulting from storm damage, just wasn't sure of the extent. They made recommendations and presented options and didn't hound the insurance company. Ultimately installed a new roof, they did great work and didn't leave a mess."
    },
    {
        "@type": "Review",
        "author": {
            "@type": "Person",
            "name": "Jeff Melching"
        },
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": "5",
            "bestRating": "5"
        },
        "reviewBody": "We had a great experience working with Evan Dozier. He has a great crew. They did great work and also an awesome cleanup. They did some repairs to wood trim in addition to the roof replacement. Target date was set at three weeks out and we started on the exact day targeted. Very professional from beginning to end."
    },
    {
        "@type": "Review",
        "author": {
            "@type": "Person",
            "name": "Carrie Brantley"
        },
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": "5",
            "bestRating": "5"
        },
        "reviewBody": "We love Mil-Spec Roofing & Construction! They are honest, on time, responsive and do high quality work. They have done maintenance on our roof and repairs for us. When it does come time to replace our roof, Mil-Spec will be our go to roof company."
    },
    {
        "@type": "Review",
        "author": {
            "@type": "Person",
            "name": "Ryan Johnson"
        },
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": "5",
            "bestRating": "5"
        },
        "reviewBody": "Great Veteran owned business! Very responsive and helpful. It's not just about the Money with the owner Evan he's there to help get what you need and comfortably. Helped me with an Inspection and quote for replacement for this tax appraisal year and he did it quick and in a hurry."
    }
]

# Pages to update
pages_to_update = [
    'index.html',
    'services/residential-roofing/index.html',
    'services/commercial-roofing/index.html',
    'services/roof-repair/index.html',
    'services/roof-replacement/index.html',
    'services/roof-installation/index.html',
    'services/roof-inspection/index.html',
    'services/emergency-roofing/index.html',
    'services/flat-roofing/index.html',
    'services/gutters-siding/index.html',
    'services/insurance-claims/index.html',
    'services/multi-family-roofing/index.html',
    'services/roof-tarping/index.html'
]

fixed_count = 0

for page in pages_to_update:
    file_path = page
    
    if not os.path.exists(file_path):
        print(f"⚠️  Skipping {page} - file not found")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the LocalBusiness schema and add review property
    # Pattern: Find the aggregateRating closing, then add review array before the closing of LocalBusiness
    
    # Find the aggregateRating section
    pattern = r'("aggregateRating":\s*\{[^}]+\})'
    
    if re.search(pattern, content):
        # Add reviews after aggregateRating
        reviews_json = json.dumps(reviews, indent=6)
        
        # Replace pattern: after aggregateRating closing }, add ,\n"review": [reviews]
        replacement = r'\1,\n      "review": ' + reviews_json
        
        content = re.sub(pattern, replacement, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        fixed_count += 1
        print(f"✅ Added reviews to {page}")
    else:
        print(f"⚠️  No aggregateRating found in {page}")

print(f"\n✅ Added review schemas to {fixed_count} pages")
print(f"📊 Each page now has 4 individual Google Review objects")
