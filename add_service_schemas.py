import os
import re

# Define schema templates for each service
service_schemas = {
    "residential-roofing": {
        "name": "Residential Roofing Services Houston TX",
        "serviceType": "Residential Roofing",
        "description": "Professional residential roofing services for homeowners in Houston and Southeast Texas. Roof replacement, repair, and installation with military-grade precision and integrity.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Modern%20Estate.jpg",
        "offers": {
            "priceRange": "$$",
            "availability": "https://schema.org/InStock"
        }
    },
    "commercial-roofing": {
        "name": "Commercial Roofing Services Houston TX",
        "serviceType": "Commercial Roofing",
        "description": "Commercial roofing contractors in Houston. TPO, EPDM, and flat roof systems for businesses, warehouses, and office complexes with professional installation and repair.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Commercial%20Complex.jpg",
        "offers": {
            "priceRange": "$$",
            "availability": "https://schema.org/InStock"
        }
    },
    "roof-repair": {
        "name": "Roof Repair Services Houston TX",
        "serviceType": "Roof Repair",
        "description": "Expert roof repair services in Houston for leaks, storm damage, and wear. Fast response times and lasting repairs backed by veteran-owned precision.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Suburban%20Storm%20Repair.jpg",
        "offers": {
            "priceRange": "$",
            "availability": "https://schema.org/InStock"
        }
    },
    "roof-replacement": {
        "name": "Roof Replacement Services Houston TX",
        "serviceType": "Roof Replacement",
        "description": "Complete roof replacement services for residential and commercial properties in Houston. High-quality materials and expert installation for long-lasting protection.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Modern%20Estate.jpg",
        "offers": {
            "priceRange": "$$$",
            "availability": "https://schema.org/InStock"
        }
    },
    "roof-installation": {
        "name": "Roof Installation Services Houston TX",
        "serviceType": "Roof Installation",
        "description": "Professional roof installation for new construction and existing properties in Houston. Precision installation with military-grade attention to detail.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Modern%20Estate.jpg",
        "offers": {
            "priceRange": "$$$",
            "availability": "https://schema.org/InStock"
        }
    },
    "flat-roofing": {
        "name": "Flat Roofing Services Houston TX",
        "serviceType": "Flat Roofing",
        "description": "Flat roofing specialists in Houston offering TPO, EPDM, and modified bitumen systems for commercial buildings and low-slope residential properties.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Commercail%20Flat%20Roof.jpg",
        "offers": {
            "priceRange": "$$",
            "availability": "https://schema.org/InStock"
        }
    },
    "multi-family-roofing": {
        "name": "Multi-Family Roofing Services Houston TX",
        "serviceType": "Multi-Family Roofing",
        "description": "Multi-family roofing solutions for apartment complexes, condos, and townhomes in Houston. Durable systems designed for property managers and HOAs.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Commercial%20Complex.jpg",
        "offers": {
            "priceRange": "$$$",
            "availability": "https://schema.org/InStock"
        }
    },
    "emergency-roofing": {
        "name": "Emergency Roofing Services Houston TX",
        "serviceType": "Emergency Roofing",
        "description": "24/7 emergency roofing services in Houston for storm damage, leaks, and urgent repairs. Fast response times when you need help immediately.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Suburban%20Storm%20Repair.jpg",
        "offers": {
            "priceRange": "$$",
            "availability": "https://schema.org/InStock"
        }
    },
    "roof-tarping": {
        "name": "Emergency Roof Tarping Services Houston TX",
        "serviceType": "Roof Tarping",
        "description": "Emergency roof tarping services in Houston to protect your property from further damage after storms. Immediate response to secure your home or business.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Suburban%20Storm%20Repair.jpg",
        "offers": {
            "priceRange": "$",
            "availability": "https://schema.org/InStock"
        }
    },
    "roof-inspection": {
        "name": "Roof Inspection Services Houston TX",
        "serviceType": "Roof Inspection",
        "description": "Professional roof inspections in Houston to assess condition, identify damage, and provide detailed reports. Free inspections available for insurance claims.",
        "image": "https://mil-specroofing.com/images/mil-specroof5.JPG",
        "offers": {
            "priceRange": "$",
            "availability": "https://schema.org/InStock"
        }
    },
    "gutters-siding": {
        "name": "Gutter and Siding Services Houston TX",
        "serviceType": "Gutters & Siding",
        "description": "Gutter installation, repair, and siding services in Houston. Protect your roof and foundation with properly functioning gutters and quality siding.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Modern%20Estate.jpg",
        "offers": {
            "priceRange": "$$",
            "availability": "https://schema.org/InStock"
        }
    },
    "insurance-claims": {
        "name": "Insurance Claims Assistance Houston TX",
        "serviceType": "Insurance Claims Assistance",
        "description": "Expert insurance claims assistance for roof damage in Houston. We work with your insurance company to ensure proper coverage and repairs.",
        "image": "https://mil-specroofing.com/images/Mil-Spec%20Roofing%20Community%20Support.jpg",
        "offers": {
            "priceRange": "$",
            "availability": "https://schema.org/InStock"
        }
    }
}

def create_service_schema(service_slug, service_data):
    """Generate JSON-LD schema for a service page"""
    schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "WebSite",
      "@id": "https://mil-specroofing.com/#website",
      "url": "https://mil-specroofing.com/",
      "name": "Mil-Spec Roofing",
      "inLanguage": "en-US",
      "publisher": {{
        "@id": "https://mil-specroofing.com/#organization"
      }}
    }},
    {{
      "@type": "WebPage",
      "@id": "https://mil-specroofing.com/services/{service_slug}/#webpage",
      "url": "https://mil-specroofing.com/services/{service_slug}/",
      "name": "{service_data['name']}",
      "description": "{service_data['description']}",
      "isPartOf": {{
        "@id": "https://mil-specroofing.com/#website"
      }},
      "about": {{
        "@id": "https://mil-specroofing.com/#organization"
      }},
      "primaryImageOfPage": {{
        "@id": "https://mil-specroofing.com/services/{service_slug}/#primaryimage"
      }}
    }},
    {{
      "@type": "ImageObject",
      "@id": "https://mil-specroofing.com/services/{service_slug}/#primaryimage",
      "url": "{service_data['image']}",
      "contentUrl": "{service_data['image']}"
    }},
    {{
      "@type": "Organization",
      "@id": "https://mil-specroofing.com/#organization",
      "name": "Mil-Spec Roofing & Construction",
      "url": "https://mil-specroofing.com/",
      "logo": {{
        "@type": "ImageObject",
        "@id": "https://mil-specroofing.com/#logo",
        "url": "https://mil-specroofing.com/images/mil-spec%20roofing%20logo.png",
        "contentUrl": "https://mil-specroofing.com/images/mil-spec%20roofing%20logo.png"
      }},
      "email": "mailto:info@mil-specroofing.com",
      "telephone": "+1-281-813-5925",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Webster",
        "addressRegion": "TX",
        "postalCode": "77598",
        "addressCountry": "US"
      }},
      "areaServed": [
        {{
          "@type": "City",
          "name": "Houston",
          "containedIn": {{
            "@type": "State",
            "name": "Texas"
          }}
        }},
        {{
          "@type": "State",
          "name": "Texas"
        }}
      ],
      "sameAs": [
        "https://www.facebook.com/MilSpecRoofing",
        "https://www.instagram.com/milspec_roofing/",
        "https://www.yelp.com/biz/mil-spec-roofing-and-construction-houston",
        "https://www.homeadvisor.com/rated.MilSpecRoofing.100009058.html",
        "https://nextdoor.com/pages/mil-spec-roofing-and-construction-houston-tx/"
      ]
    }},
    {{
      "@type": "Service",
      "@id": "https://mil-specroofing.com/services/{service_slug}/#service",
      "name": "{service_data['name']}",
      "serviceType": "{service_data['serviceType']}",
      "description": "{service_data['description']}",
      "provider": {{
        "@id": "https://mil-specroofing.com/#organization"
      }},
      "areaServed": {{
        "@type": "State",
        "name": "Texas"
      }},
      "hasOfferCatalog": {{
        "@type": "OfferCatalog",
        "name": "{service_data['serviceType']} Services",
        "itemListElement": [
          {{
            "@type": "Offer",
            "itemOffered": {{
              "@type": "Service",
              "name": "{service_data['name']}"
            }},
            "priceRange": "{service_data['offers']['priceRange']}",
            "availability": "{service_data['offers']['availability']}"
          }}
        ]
      }}
    }},
    {{
      "@type": "LocalBusiness",
      "@id": "https://mil-specroofing.com/#localbusiness",
      "name": "Mil-Spec Roofing & Construction",
      "image": "{service_data['image']}",
      "telephone": "+1-281-813-5925",
      "email": "info@mil-specroofing.com",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "",
        "addressLocality": "Webster",
        "addressRegion": "TX",
        "postalCode": "77598",
        "addressCountry": "US"
      }},
      "priceRange": "{service_data['offers']['priceRange']}",
      "openingHoursSpecification": [
        {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "08:00",
          "closes": "18:00"
        }},
        {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": "Saturday",
          "opens": "09:00",
          "closes": "16:00"
        }}
      ]
    }}
  ]
}}
</script>
'''
    return schema

def add_schema_to_service_page(file_path, service_slug):
    """Add JSON-LD schema to a service page"""
    try:
        if service_slug not in service_schemas:
            print(f"No schema defined for {service_slug}")
            return False
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if schema already exists
        if 'application/ld+json' in content:
            print(f"Schema already exists in {file_path}")
            return False
        
        # Generate schema
        schema = create_service_schema(service_slug, service_schemas[service_slug])
        
        # Insert schema right after <head> tag
        content = content.replace('<head>', f'<head>\n{schema}')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# Process all service pages
services_dir = './services'
updated_count = 0

for service_slug in service_schemas.keys():
    file_path = os.path.join(services_dir, service_slug, 'index.html')
    if os.path.exists(file_path):
        if add_schema_to_service_page(file_path, service_slug):
            updated_count += 1
            print(f"✓ Added schema to {service_slug}")
    else:
        print(f"✗ File not found: {file_path}")

print(f"\n✓ Added schemas to {updated_count}/{len(service_schemas)} service pages")
