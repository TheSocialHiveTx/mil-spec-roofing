// --- Initialization ---
document.addEventListener('DOMContentLoaded', () => {
    // Initialize Icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // --- Data for Modals Only ---
    const serviceData = {
      residential: {
        title: 'Residential Roofing',
        icon: 'home',
        longDescription: "Your home is your sanctuary, and the roof is its first line of defense. We specialize in high-performance residential roofing systems that blend aesthetic appeal with military-grade precision installation. Whether you prefer architectural shingles, impact-resistant synthetic slate, or standing seam metal, our installation process is rigorous, documented, and backed by a workmanship guarantee.",
        benefits: ["Lifetime Manufacturer Warranties", "Class 4 Impact Resistance", "Enhanced Ventilation", "Flawless Cleanup"]
      },
      commercial: {
        title: 'Commercial Roofing',
        icon: 'hard-hat',
        longDescription: "Business continuity relies on a secure facility. Our commercial division handles complex flat roof systems including TPO, EPDM, and PVC. We understand the unique challenges of commercial properties, from HVAC integration to drainage optimization, ensuring minimal disruption to your daily operations during installation.",
        benefits: ["Energy-Efficient Cool Roofs", "NDL Warranties", "Preventative Maintenance", "High-Traffic Walkpads"]
      },
      repair: {
        title: 'Storm Damage Repair',
        icon: 'wrench',
        longDescription: "When nature strikes, time is the enemy. Our Rapid Response Team creates an immediate perimeter to prevent further water intrusion. We then perform a forensic-level assessment to document all damage for insurance purposes, ensuring nothing is overlooked. From hail dents to wind-lifted shingles, we restore the integrity of your shelter.",
        benefits: ["24/7 Emergency Tarping", "Forensic Damage Assessment", "Insurance Adjuster Coordination", "Fast-Track Scheduling"]
      },
      inspection: {
        title: 'Mil-Spec Inspection',
        icon: 'shield',
        longDescription: "Don't wait for a leak to reveal a weakness. Our Mil-Spec 21-Point Inspection is a tactical assessment of your roof's integrity. We use drone technology and thermal imaging to detect subsurface moisture and structural anomalies that the naked eye misses. You receive a comprehensive digital report with graded priorities.",
        benefits: ["Drone Aerial Analysis", "Thermal Moisture Detection", "Detailed Photo Report", "3-5 Year Lifespan Projections"]
      },
      gutters: {
        title: 'Gutters & Siding',
        icon: 'ruler',
        longDescription: "Water management is critical to foundation health. Our seamless gutter systems are fabricated on-site for a perfect fit, eliminating leak points. Coupled with our high-durability siding options, we harden your home's exterior envelope against wind, rain, and thermal bridging.",
        benefits: ["Seamless Aluminum & Copper", "Leaf Guard Protection", "HardieBoard & Vinyl Siding", "Rot Repair"]
      },
      insurance: {
        title: 'Insurance Claims',
        icon: 'umbrella',
        longDescription: "The insurance battlefield is complex and bureaucratic. We act as your advocate, translating technical roofing data into the language adjusters understand. We ensure your policy is honored to its full extent, covering not just the roof, but all collateral damage including gutters, screens, and fences.",
        benefits: ["Xactimate Estimates", "Code Upgrade Coverage", "Supplemental Documentation", "Zero-Stress Paperwork"]
      }
    };

    const galleryImages = [
        { title: 'Modern Estate Replacement', type: 'Residential', img: 'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' },
        { title: 'Commercial Complex', type: 'Commercial', img: 'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' },
        { title: 'Suburban Storm Repair', type: 'Repair', img: 'https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' },
        { title: 'Luxury Metal Seam', type: 'Specialty', img: 'https://images.pexels.com/photos/259950/pexels-photo-259950.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' },
        { title: 'Historic Restoration', type: 'Restoration', img: 'https://images.pexels.com/photos/209296/pexels-photo-209296.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' },
        { title: 'Industrial Flat Roof', type: 'Commercial', img: 'https://images.pexels.com/photos/176342/pexels-photo-176342.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' }
    ];

    const testimonials = [
      { name: "Michael R.", role: "Homeowner", content: "The level of discipline this crew showed was incredible. They arrived at 0700 sharp, worked efficiently, and left my yard cleaner than they found it. The roof looks amazing.", rating: 5 },
      { name: "Sarah Jenkins", role: "Property Manager", content: "I manage 15 commercial properties. Mil-Spec is the only team I trust. Their reports are detailed, their pricing is transparent, and their work holds up to Texas storms.", rating: 5 },
      { name: "David Chen", role: "Business Owner", content: "We had a massive leak during the spring rains. Their rapid response team was onsite within 2 hours. They tarped it, quoted it, and fixed it within the week.", rating: 5 }
    ];

    // --- Navbar Logic ---
    const navbar = document.getElementById('navbar');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                navbar.classList.add('shadow-md', 'py-2');
                navbar.classList.remove('py-4');
            } else {
                navbar.classList.remove('shadow-md', 'py-2');
                navbar.classList.add('py-4');
            }
        });
    }

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if (mobileMenu) mobileMenu.classList.add('hidden');
        });
    });

    // --- Services Modal Logic ---
    const serviceModal = document.getElementById('service-modal');
    const serviceModalContent = document.getElementById('service-modal-content');
    const closeModalOverlay = document.getElementById('close-modal-overlay');

    // Attach click events to static service cards
    document.querySelectorAll('.service-card').forEach(card => {
        card.addEventListener('click', () => {
            const id = card.getAttribute('data-id');
            const data = serviceData[id];
            if (data) openModal(data);
        });
    });

    function openModal(service) {
        if (!serviceModal || !serviceModalContent) return;

        const benefitsHtml = service.benefits.map(b => `<li class="flex items-start mb-2"><i data-lucide="check" class="h-5 w-5 text-blue-500 mr-2 mt-0.5"></i><span class="text-slate-600">${b}</span></li>`).join('');
        
        serviceModalContent.innerHTML = `
            <div class="bg-slate-50 p-6 border-b border-slate-100 flex justify-between items-start sticky top-0 z-20">
                 <div class="flex items-center space-x-4">
                    <div class="p-3 bg-blue-100 text-blue-600 rounded-lg">
                      <i data-lucide="${service.icon}" class="h-8 w-8"></i>
                    </div>
                    <div>
                      <h3 class="text-2xl font-bold text-slate-900">${service.title}</h3>
                      <p class="text-slate-500 text-sm uppercase tracking-wider font-semibold">Service Briefing</p>
                    </div>
                 </div>
                 <button id="modal-close-btn" class="p-2 hover:bg-slate-200 rounded-full">
                    <i data-lucide="x" class="h-6 w-6 text-slate-500"></i>
                 </button>
            </div>
            <div class="p-6">
                <p class="text-lg text-slate-700 leading-relaxed mb-8">${service.longDescription}</p>
                <h4 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-4 border-b pb-2">Key Benefits</h4>
                <ul class="mb-8 list-none pl-0">${benefitsHtml}</ul>
                <div class="flex gap-4">
                     <button id="modal-req-btn" class="flex-1 bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-lg font-bold uppercase tracking-wider">Request This Service</button>
                </div>
            </div>
        `;
        serviceModal.classList.remove('hidden');
        serviceModal.classList.add('flex');
        document.body.style.overflow = 'hidden';
        if (typeof lucide !== 'undefined') lucide.createIcons();

        document.getElementById('modal-close-btn').onclick = () => {
            serviceModal.classList.add('hidden');
            document.body.style.overflow = 'unset';
        };
        document.getElementById('modal-req-btn').onclick = () => {
            serviceModal.classList.add('hidden');
            document.body.style.overflow = 'unset';
            document.getElementById('contact').scrollIntoView({behavior: 'smooth'});
        };
    }

    if (closeModalOverlay) {
        closeModalOverlay.onclick = () => {
            serviceModal.classList.add('hidden');
            document.body.style.overflow = 'unset';
        };
    }

    // --- Gallery Generation & Lightbox ---
    const galleryGrid = document.getElementById('gallery-grid');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');

    if (galleryGrid && lightbox) {
        galleryImages.forEach(img => {
            const el = document.createElement('div');
            el.className = 'group relative rounded-lg overflow-hidden shadow-md cursor-pointer h-72';
            el.innerHTML = `
                <img src="${img.img}" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" />
                <div class="absolute inset-0 bg-slate-900/0 group-hover:bg-slate-900/40 transition-colors duration-300"></div>
                <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <div class="bg-white/20 backdrop-blur-sm p-3 rounded-full"><i data-lucide="zoom-in" class="text-white h-8 w-8"></i></div>
                </div>
                <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-slate-900 via-slate-900/80 to-transparent p-6 translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                    <span class="text-blue-400 text-xs font-bold uppercase tracking-wider mb-1 block">${img.type}</span>
                    <h3 class="text-white text-xl font-bold">${img.title}</h3>
                </div>
            `;
            el.onclick = () => {
                lightboxImg.src = img.img;
                lightboxCaption.textContent = img.title;
                lightbox.classList.remove('hidden');
                lightbox.classList.add('flex');
                document.body.style.overflow = 'hidden';
            };
            galleryGrid.appendChild(el);
        });

        const closeBtn = document.getElementById('close-lightbox');
        if(closeBtn) {
            closeBtn.onclick = () => {
                lightbox.classList.add('hidden');
                document.body.style.overflow = 'unset';
            };
        }
    }

    // --- Testimonials Carousel ---
    const testimonialContent = document.getElementById('testimonial-content');
    if (testimonialContent) {
        let currentTestimonial = 0;

        function updateTestimonial() {
            const t = testimonials[currentTestimonial];
            const stars = Array(t.rating).fill('<i data-lucide="star" class="h-6 w-6 text-yellow-400 fill-current inline-block"></i>').join(' ');
            testimonialContent.style.opacity = '0';
            setTimeout(() => {
                testimonialContent.innerHTML = `
                    <div class="flex justify-center mb-6 space-x-1">${stars}</div>
                    <p class="text-xl md:text-2xl text-slate-700 text-center font-medium leading-relaxed italic mb-8">"${t.content}"</p>
                    <div class="text-center">
                        <h4 class="text-lg font-bold text-slate-900">${t.name}</h4>
                        <p class="text-blue-600 text-sm font-semibold uppercase tracking-wide">${t.role}</p>
                    </div>
                `;
                if (typeof lucide !== 'undefined') lucide.createIcons();
                testimonialContent.style.opacity = '1';
            }, 200);
        }

        const nextBtn = document.getElementById('next-testimonial');
        const prevBtn = document.getElementById('prev-testimonial');

        if(nextBtn) nextBtn.onclick = () => {
            currentTestimonial = (currentTestimonial + 1) % testimonials.length;
            updateTestimonial();
        };

        if(prevBtn) prevBtn.onclick = () => {
            currentTestimonial = (currentTestimonial === 0) ? testimonials.length - 1 : currentTestimonial - 1;
            updateTestimonial();
        };

        updateTestimonial();
        // Auto advance
        setInterval(() => {
            currentTestimonial = (currentTestimonial + 1) % testimonials.length;
            updateTestimonial();
        }, 6000);
    }

    // --- Animated Counters ---
    const aboutSection = document.getElementById('about');
    if (aboutSection) {
        const counters = [
            { id: 'counter-years', end: 18 },
            { id: 'counter-missions', end: 2540, suffix: '' },
            { id: 'counter-satisfaction', end: 100, suffix: '%' }
        ];
        let countersStarted = false;

        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !countersStarted) {
                countersStarted = true;
                counters.forEach(c => {
                    const el = document.getElementById(c.id);
                    if (!el) return;
                    
                    let start = 0;
                    const duration = 2000;
                    const startTime = performance.now();
                    
                    function update(currentTime) {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const easeOut = 1 - Math.pow(1 - progress, 4);
                        
                        const currentVal = Math.floor(easeOut * c.end);
                        el.innerText = currentVal + (c.suffix || (c.id === 'counter-years' ? '+' : '')); // preserve suffix
                        
                        if (progress < 1) requestAnimationFrame(update);
                    }
                    requestAnimationFrame(update);
                });
            }
        }, { threshold: 0.5 });
        observer.observe(aboutSection);
    }
});