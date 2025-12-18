import React, { useState } from 'react';
import { Home, Shield, Wrench, Umbrella, Ruler, HardHat, X, Check, ArrowRight, FileText } from 'lucide-react';
import { SectionId, ServiceItem } from '../types';

const services: ServiceItem[] = [
  {
    id: 'residential',
    title: 'Residential Roofing',
    description: 'Complete roof replacements using premium asphalt, metal, or tile materials with industry-leading warranties.',
    iconName: 'Home',
    longDescription: "Your home is your sanctuary, and the roof is its first line of defense. We specialize in high-performance residential roofing systems that blend aesthetic appeal with military-grade precision installation. Whether you prefer architectural shingles, impact-resistant synthetic slate, or standing seam metal, our installation process is rigorous, documented, and backed by a workmanship guarantee.",
    benefits: [
      "Lifetime Manufacturer Warranties",
      "Class 4 Impact Resistance Options",
      "Enhanced Ventilation Systems",
      "Flawless Cleanup Protocol (Magnetic Sweeps)"
    ],
    caseStudy: {
      title: "The Anderson Estate",
      summary: "Replaced a failing 20-year-old roof with slate-composite shingles, increasing the home's appraisal value by 12% and reducing insurance premiums."
    }
  },
  {
    id: 'commercial',
    title: 'Commercial Roofing',
    description: 'Flat roof solutions (TPO, EPDM) designed for durability and energy efficiency for your business.',
    iconName: 'HardHat',
    longDescription: "Business continuity relies on a secure facility. Our commercial division handles complex flat roof systems including TPO, EPDM, and PVC. We understand the unique challenges of commercial properties, from HVAC integration to drainage optimization, ensuring minimal disruption to your daily operations during installation.",
    benefits: [
      "Energy-Efficient Cool Roofs",
      "NDL (No Dollar Limit) Warranties",
      "Preventative Maintenance Plans",
      "High-Traffic Walkpads & Safety Systems"
    ],
    caseStudy: {
      title: "Logistics Hub Alpha",
      summary: "Installed a 50,000 sq ft TPO system while the facility remained fully operational. The new reflective surface reduced cooling costs by 25%."
    }
  },
  {
    id: 'repair',
    title: 'Storm Damage Repair',
    description: 'Rapid response teams for leak detection, shingle replacement, and emergency storm damage mitigation.',
    iconName: 'Wrench',
    longDescription: "When nature strikes, time is the enemy. Our Rapid Response Team creates an immediate barrier to prevent further water intrusion. We then perform a forensic-level assessment to document all damage for insurance purposes, ensuring nothing is overlooked. From hail dents to wind-lifted shingles, we restore the integrity of your shelter.",
    benefits: [
      "24/7 Emergency Tarping",
      "Forensic Damage Assessment",
      "Insurance Adjuster Coordination",
      "Fast-Track Scheduling for Vulnerable Homes"
    ],
    caseStudy: {
      title: "Sector 7 Hail Response",
      summary: "Successfully restored 15 homes in a single subdivision within 3 weeks of a catastrophic hail event, coordinating directly with 8 different insurance carriers."
    }
  },
  {
    id: 'inspection',
    title: 'Mil-Spec Inspection',
    description: 'Detailed multipoint inspections to identify potential issues before they become costly failures.',
    iconName: 'Shield',
    longDescription: "Don't wait for a leak to reveal a weakness. Our Mil-Spec multi-point inspection is a tactical assessment of your roof's integrity. We use drone technology and thermal imaging to detect subsurface moisture and structural anomalies that the naked eye misses. You receive a comprehensive digital report with graded priorities.",
    benefits: [
      "Drone Aerial Analysis",
      "Detailed Photo Report with Action Plan",
      "3-5 Year Lifespan Projections"
    ],
    caseStudy: {
      title: "Retail Plaza Audit",
      summary: "Identified 6 critical failure points in a 'new' roof installed by a competitor, saving the owner an estimated $100k in potential water damage repairs."
    }
  },
  {
    id: 'gutters',
    title: 'Gutters & Siding',
    description: 'Seamless gutter installation and premium siding solutions to protect your home\'s exterior envelope.',
    iconName: 'Ruler',
    longDescription: "Water management is critical to foundation health. Our seamless gutter systems are fabricated on-site for a perfect fit, eliminating leak points. Coupled with our high-durability siding options (Fiber Cement or Vinyl), we harden your home's exterior envelope against wind, rain, and thermal bridging.",
    benefits: [
      "Seamless Aluminum Gutters",
      "Advanced Leaf Guard Protection",
      "HardieBoard & Vinyl Siding Installation",
      "Fascia & Soffit Rot Repair"
    ],
    caseStudy: {
      title: "Hilltop Residence",
      summary: "Resolved chronic basement flooding by redesigning the gutter drainage system with 6-inch seamless gutters and strategic downspout placement."
    }
  },
  {
    id: 'insurance',
    title: 'Insurance Claims',
    description: 'We navigate the complex insurance process for you, ensuring you get the full coverage you deserve.',
    iconName: 'Umbrella',
    longDescription: "The insurance battlefield is complex and bureaucratic. We act as your advocate, translating technical roofing data into the language adjusters understand. We ensure your policy is honored to its full extent, covering not just the roof, but all collateral damage including gutters, screens, and fences.",
    benefits: [
      "Xactimate Estimates (Industry Standard)",
      "Code Upgrade Coverage Assistance",
      "Supplemental Damage Documentation",
      "Zero-Stress Paperwork Handling"
    ],
    caseStudy: {
      title: "Claim #4092",
      summary: "Overturned an initial denial for wind damage, securing a full roof replacement coverage of $22,000 for the homeowner through detailed photo evidence."
    }
  }
];

const IconMap: Record<string, React.ElementType> = {
  Home, Shield, Wrench, Umbrella, Ruler, HardHat
};

const Services: React.FC = () => {
  const [selectedService, setSelectedService] = useState<ServiceItem | null>(null);

  const openModal = (service: ServiceItem) => {
    setSelectedService(service);
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
  };

  const closeModal = () => {
    setSelectedService(null);
    document.body.style.overflow = 'unset';
  };

  return (
    <section id={SectionId.SERVICES} className="py-24 bg-white relative">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Mission Ready <span className="text-blue-600">Services</span>
          </h2>
          <div className="h-1 w-20 bg-blue-600 mx-auto rounded-full mb-6"></div>
          <p className="text-slate-600 max-w-2xl mx-auto text-lg">
            From minor repairs to major installations, we execute every project with military precision. Click on any service for a detailed briefing.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service) => {
            const Icon = IconMap[service.iconName];
            return (
              <div
                key={service.id}
                onClick={() => openModal(service)}
                className="group bg-slate-50 p-8 rounded-lg border border-slate-100 hover:border-blue-500 hover:shadow-xl transition-all duration-300 relative overflow-hidden cursor-pointer flex flex-col h-full"
              >
                <div className="absolute top-0 left-0 w-2 h-full bg-blue-600 transform -translate-x-full group-hover:translate-x-0 transition-transform duration-300"></div>

                <div className="mb-6 inline-block p-4 bg-white rounded-full shadow-sm text-blue-600 group-hover:bg-blue-600 group-hover:text-white transition-colors duration-300 w-16 h-16 flex items-center justify-center">
                  <Icon className="h-8 w-8" />
                </div>

                <h3 className="text-xl font-bold text-slate-900 mb-3 group-hover:text-blue-600 transition-colors">
                  {service.title}
                </h3>

                <p className="text-slate-600 leading-relaxed mb-6 flex-grow">
                  {service.description}
                </p>

                <div className="flex items-center text-blue-600 font-semibold text-sm uppercase tracking-wide opacity-0 group-hover:opacity-100 transition-opacity duration-300 transform translate-y-2 group-hover:translate-y-0">
                  View Details <ArrowRight className="ml-2 h-4 w-4" />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Modal Overlay */}
      {selectedService && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center p-4">
          <div
            className="absolute inset-0 bg-slate-900/80 backdrop-blur-sm transition-opacity"
            onClick={closeModal}
          ></div>

          <div className="bg-white rounded-2xl shadow-2xl w-full max-w-3xl max-h-[90vh] overflow-y-auto relative z-10 animate-in fade-in zoom-in duration-200">
            {/* Modal Header */}
            <div className="bg-slate-50 p-6 md:p-8 border-b border-slate-100 flex justify-between items-start sticky top-0 z-20">
              <div className="flex items-center space-x-4">
                <div className="p-3 bg-blue-100 text-blue-600 rounded-lg">
                  {React.createElement(IconMap[selectedService.iconName], { className: "h-8 w-8" })}
                </div>
                <div>
                  <h3 className="text-2xl font-bold text-slate-900">{selectedService.title}</h3>
                  <p className="text-slate-500 text-sm uppercase tracking-wider font-semibold">Service Briefing</p>
                </div>
              </div>
              <button
                onClick={closeModal}
                className="p-2 hover:bg-slate-200 rounded-full transition-colors"
              >
                <X className="h-6 w-6 text-slate-500" />
              </button>
            </div>

            {/* Modal Content */}
            <div className="p-6 md:p-8">
              <div className="prose max-w-none mb-8">
                <p className="text-lg text-slate-700 leading-relaxed">
                  {selectedService.longDescription}
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                <div>
                  <h4 className="text-sm font-bold text-slate-900 uppercase tracking-wider mb-4 border-b pb-2">Key Benefits</h4>
                  <ul className="space-y-3">
                    {selectedService.benefits.map((benefit, index) => (
                      <li key={index} className="flex items-start">
                        <Check className="h-5 w-5 text-blue-500 mr-2 flex-shrink-0 mt-0.5" />
                        <span className="text-slate-600">{benefit}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {selectedService.caseStudy && (
                  <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
                    <div className="flex items-center space-x-2 mb-3">
                      <FileText className="h-5 w-5 text-blue-600" />
                      <h4 className="text-sm font-bold text-slate-900 uppercase tracking-wider">Case Study</h4>
                    </div>
                    <h5 className="font-bold text-slate-900 mb-2">{selectedService.caseStudy.title}</h5>
                    <p className="text-sm text-slate-600 italic">"{selectedService.caseStudy.summary}"</p>
                  </div>
                )}
              </div>

              <div className="flex flex-col sm:flex-row gap-4 pt-4 border-t border-slate-100">
                <button
                  onClick={() => {
                    closeModal();
                    document.getElementById(SectionId.CONTACT)?.scrollIntoView({ behavior: 'smooth' });
                  }}
                  className="flex-1 bg-blue-600 hover:bg-blue-700 text-white py-4 px-6 rounded-lg font-bold uppercase tracking-wider transition-colors shadow-lg hover:shadow-blue-500/25 text-center"
                >
                  Request This Service
                </button>
                <button
                  onClick={closeModal}
                  className="flex-1 bg-white border-2 border-slate-200 hover:border-slate-300 text-slate-700 py-4 px-6 rounded-lg font-bold uppercase tracking-wider transition-colors text-center"
                >
                  Close Briefing
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </section>
  );
};

export default Services;
