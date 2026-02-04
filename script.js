document.addEventListener('DOMContentLoaded', () => {

    // --- 1. Initialize Icons ---
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // --- 3. Data: Gallery Images (Keep for Lightbox) ---
    const galleryImages = [
        { title: 'Modern Estate Replacement', type: 'Residential', img: '/images/Mil-Spec Roofing Modern Estate.jpg' },
        { title: 'Commercial Complex', type: 'Commercial', img: '/images/Mil-Spec Roofing Commercial Complex.jpg' },
        { title: 'Suburban Storm Repair', type: 'Repair', img: '/images/Mil-Spec Roofing Suburban Storm Repair.jpg' },
        { title: 'Luxury Metal Seam', type: 'Specialty', img: '/images/Mil-Spec Roofing Metal Roofing.jpg' },
        { title: 'Community Support', type: 'Restoration', img: '/images/Mil-Spec Roofing Community Support.jpg' },
        { title: 'Industrial Flat Roof', type: 'Commercial', img: '/images/Mil-Spec Roofing Commercail Flat Roof.jpg' }
    ];

    // --- 4. Data: Testimonials (Keep for Carousel) ---
    const testimonials = [
        { name: "Michael R.", role: "Homeowner", content: "The level of discipline this crew showed was incredible. They arrived at 0700 sharp, worked efficiently, and left my yard cleaner than they found it. The roof looks amazing.", rating: 5 },
        { name: "Sarah Jenkins", role: "Property Manager", content: "I manage 15 commercial properties. Mil-Spec is the only team I trust. Their reports are detailed, their pricing is transparent, and their work holds up to Texas storms.", rating: 5 },
        { name: "David Chen", role: "Business Owner", content: "We had a massive leak during the spring rains. Their rapid response team was onsite within 2 hours. They tarped it, quoted it, and fixed it within the week.", rating: 5 }
    ];

    // --- 5. Navbar Logic ---
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

    // --- 7. Gallery Generation & Lightbox ---
    const galleryGrid = document.getElementById('gallery-grid');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');

    if (galleryGrid && lightbox) {
        galleryGrid.innerHTML = ''; // Ensure grid is clear before adding
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
        if (closeBtn) {
            closeBtn.onclick = () => {
                lightbox.classList.add('hidden');
                document.body.style.overflow = 'unset';
            };
        }
    }

    // --- 8. Testimonials Logic ---
    const testimonialContent = document.getElementById('testimonial-content');
    if (testimonialContent) {
        let currentTestimonial = 0;

        function updateTestimonial() {
            const t = testimonials[currentTestimonial];
            if (!t) return;

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

        if (nextBtn) nextBtn.onclick = () => {
            currentTestimonial = (currentTestimonial + 1) % testimonials.length;
            updateTestimonial();
        };

        if (prevBtn) prevBtn.onclick = () => {
            currentTestimonial = (currentTestimonial === 0) ? testimonials.length - 1 : currentTestimonial - 1;
            updateTestimonial();
        };

        updateTestimonial();
        setInterval(() => {
            currentTestimonial = (currentTestimonial + 1) % testimonials.length;
            updateTestimonial();
        }, 6000);
    }

    // --- 9. Animated Counters ---
    const aboutSection = document.getElementById('about');
    if (aboutSection) {
        const counters = [
            { id: 'counter-years', end: 10, suffix: '+' },
            { id: 'counter-missions', end: 250, suffix: '+' },
            { id: 'counter-satisfaction', end: 100, suffix: '%' }
        ];
        let countersStarted = false;

        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !countersStarted) {
                countersStarted = true;
                counters.forEach(c => {
                    const el = document.getElementById(c.id);
                    if (!el) return;

                    const duration = 2000;
                    const startTime = performance.now();

                    function update(currentTime) {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const easeOut = 1 - Math.pow(1 - progress, 4);

                        const currentVal = Math.floor(easeOut * c.end);
                        el.innerText = currentVal + (c.suffix || '');

                        if (progress < 1) requestAnimationFrame(update);
                    }
                    requestAnimationFrame(update);
                });
            }
        }, { threshold: 0.5 });
        observer.observe(aboutSection);
    }
});
