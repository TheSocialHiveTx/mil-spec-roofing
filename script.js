import { GoogleGenAI } from "@google/genai";

// Initialize Icons
lucide.createIcons();

// --- Data ---
const services = [
  {
    id: 'residential',
    title: 'Residential Roofing',
    description: 'Complete roof replacements using premium asphalt, metal, or tile materials with industry-leading warranties.',
    icon: 'home',
    longDescription: "Your home is your sanctuary, and the roof is its first line of defense. We specialize in high-performance residential roofing systems that blend aesthetic appeal with military-grade durability.",
    benefits: ["Lifetime Manufacturer Warranties", "Class 4 Impact Resistance", "Enhanced Ventilation", "Flawless Cleanup"]
  },
  {
    id: 'commercial',
    title: 'Commercial Roofing',
    description: 'Flat roof solutions (TPO, EPDM) designed for durability and energy efficiency for your business.',
    icon: 'hard-hat',
    longDescription: "Business continuity relies on a secure facility. Our commercial division handles complex flat roof systems including TPO, EPDM, and PVC.",
    benefits: ["Energy-Efficient Cool Roofs", "NDL Warranties", "Preventative Maintenance", "High-Traffic Walkpads"]
  },
  {
    id: 'repair',
    title: 'Storm Damage Repair',
    description: 'Rapid response teams for leak detection, shingle replacement, and emergency storm damage mitigation.',
    icon: 'wrench',
    longDescription: "When nature strikes, time is the enemy. Our Rapid Response Team creates an immediate perimeter to prevent further water intrusion.",
    benefits: ["24/7 Emergency Tarping", "Forensic Damage Assessment", "Insurance Adjuster Coordination", "Fast-Track Scheduling"]
  },
  {
    id: 'inspection',
    title: 'Mil-Spec Inspection',
    description: 'Detailed 21-point roof inspections to identify potential issues before they become costly failures.',
    icon: 'shield',
    longDescription: "Don't wait for a leak to reveal a weakness. Our Mil-Spec 21-Point Inspection is a tactical assessment of your roof's integrity.",
    benefits: ["Drone Aerial Analysis", "Thermal Moisture Detection", "Detailed Photo Report", "3-5 Year Lifespan Projections"]
  },
  {
    id: 'gutters',
    title: 'Gutters & Siding',
    description: 'Seamless gutter installation and premium siding solutions to protect your home\'s exterior envelope.',
    icon: 'ruler',
    longDescription: "Water management is critical to foundation health. Our seamless gutter systems are fabricated on-site for a perfect fit.",
    benefits: ["Seamless Aluminum & Copper", "Leaf Guard Protection", "HardieBoard & Vinyl Siding", "Rot Repair"]
  },
  {
    id: 'insurance',
    title: 'Insurance Claims',
    description: 'We navigate the complex insurance process for you, ensuring you get the full coverage you deserve.',
    icon: 'umbrella',
    longDescription: "The insurance battlefield is complex. We act as your advocate, translating technical roofing data into language adjusters understand.",
    benefits: ["Xactimate Estimates", "Code Upgrade Coverage", "Supplemental Documentation", "Zero-Stress Paperwork"]
  }
];

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

window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
        navbar.classList.add('shadow-md', 'py-2');
        navbar.classList.remove('py-4');
    } else {
        navbar.classList.remove('shadow-md', 'py-2');
        navbar.classList.add('py-4');
    }
    
    // Scroll Spy
    const sections = ['home', 'services', 'about', 'gallery', 'contact'];
    sections.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            const rect = el.getBoundingClientRect();
            if (rect.top <= 150 && rect.bottom >= 150) {
                 document.querySelectorAll('.nav-link').forEach(link => {
                     link.classList.remove('text-blue-600');
                     link.classList.add('text-slate-600');
                     if(link.getAttribute('href') === `#${id}`) {
                         link.classList.add('text-blue-600');
                         link.classList.remove('text-slate-600');
                     }
                 });
            }
        }
    });
});

mobileMenuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// Close mobile menu on click
document.querySelectorAll('.mobile-nav-link').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
    });
});

// --- Services Generation & Modal ---
const servicesGrid = document.getElementById('services-grid');
const serviceModal = document.getElementById('service-modal');
const serviceModalContent = document.getElementById('service-modal-content');
const closeModalOverlay = document.getElementById('close-modal-overlay');

services.forEach(service => {
    const card = document.createElement('div');
    card.className = 'group bg-slate-50 p-8 rounded-lg border border-slate-100 hover:border-blue-500 hover:shadow-xl transition-all duration-300 relative overflow-hidden cursor-pointer flex flex-col h-full';
    card.innerHTML = `
        <div class="absolute top-0 left-0 w-2 h-full bg-blue-600 transform -translate-x-full group-hover:translate-x-0 transition-transform duration-300"></div>
        <div class="mb-6 inline-block p-4 bg-white rounded-full shadow-sm text-blue-600 group-hover:bg-blue-600 group-hover:text-white transition-colors duration-300 w-16 h-16 flex items-center justify-center">
            <i data-lucide="${service.icon}" class="h-8 w-8"></i>
        </div>
        <h3 class="text-xl font-bold text-slate-900 mb-3 group-hover:text-blue-600 transition-colors">${service.title}</h3>
        <p class="text-slate-600 leading-relaxed mb-6 flex-grow">${service.description}</p>
        <div class="flex items-center text-blue-600 font-semibold text-sm uppercase tracking-wide opacity-0 group-hover:opacity-100 transition-opacity duration-300 transform translate-y-2 group-hover:translate-y-0">
            View Details <i data-lucide="arrow-right" class="ml-2 h-4 w-4"></i>
        </div>
    `;
    card.onclick = () => openModal(service);
    servicesGrid.appendChild(card);
});

function openModal(service) {
    const benefitsHtml = service.benefits.map(b => `<li class="flex items-start"><i data-lucide="check" class="h-5 w-5 text-blue-500 mr-2 mt-0.5"></i><span class="text-slate-600">${b}</span></li>`).join('');
    
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
             <button onclick="document.getElementById('service-modal').classList.add('hidden'); document.body.style.overflow = 'unset';" class="p-2 hover:bg-slate-200 rounded-full">
                <i data-lucide="x" class="h-6 w-6 text-slate-500"></i>
             </button>
        </div>
        <div class="p-6">
            <p class="text-lg text-slate-700 leading-relaxed mb-8">${service.longDescription}</p>
            <h4 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-4 border-b pb-2">Key Benefits</h4>
            <ul class="space-y-3 mb-8">${benefitsHtml}</ul>
            <div class="flex gap-4">
                 <button onclick="document.getElementById('service-modal').classList.add('hidden'); document.body.style.overflow = 'unset'; document.getElementById('contact').scrollIntoView({behavior: 'smooth'})" class="flex-1 bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-lg font-bold uppercase tracking-wider">Request This Service</button>
            </div>
        </div>
    `;
    serviceModal.classList.remove('hidden');
    serviceModal.classList.add('flex');
    document.body.style.overflow = 'hidden';
    lucide.createIcons();
}

closeModalOverlay.onclick = () => {
    serviceModal.classList.add('hidden');
    document.body.style.overflow = 'unset';
};

// --- Gallery Generation & Lightbox ---
const galleryGrid = document.getElementById('gallery-grid');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxCaption = document.getElementById('lightbox-caption');

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

document.getElementById('close-lightbox').onclick = () => {
    lightbox.classList.add('hidden');
    document.body.style.overflow = 'unset';
};

// --- Testimonials Carousel ---
let currentTestimonial = 0;
const testimonialContent = document.getElementById('testimonial-content');

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
        lucide.createIcons();
        testimonialContent.style.opacity = '1';
    }, 200);
}

document.getElementById('next-testimonial').onclick = () => {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    updateTestimonial();
};
document.getElementById('prev-testimonial').onclick = () => {
    currentTestimonial = (currentTestimonial === 0) ? testimonials.length - 1 : currentTestimonial - 1;
    updateTestimonial();
};
updateTestimonial();
setInterval(() => {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    updateTestimonial();
}, 6000);

// --- Animated Counters ---
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
observer.observe(document.getElementById('about'));


// --- AI Consultant ---
const aiBtn = document.getElementById('ai-toggle-btn');
const aiWindow = document.getElementById('ai-chat-window');
const chatInput = document.getElementById('chat-input');
const chatSend = document.getElementById('chat-send-btn');
const chatMessages = document.getElementById('chat-messages');

aiBtn.onclick = () => {
    aiWindow.classList.toggle('hidden');
    const icon = aiBtn.querySelector('svg');
    if (aiWindow.classList.contains('hidden')) {
        aiBtn.classList.remove('bg-red-500', 'rotate-90');
        aiBtn.classList.add('bg-blue-600');
        aiBtn.innerHTML = '<i data-lucide="message-square" class="text-white h-6 w-6"></i>';
    } else {
        aiBtn.classList.add('bg-red-500', 'rotate-90');
        aiBtn.classList.remove('bg-blue-600');
        aiBtn.innerHTML = '<i data-lucide="x" class="text-white h-6 w-6"></i>';
    }
    lucide.createIcons();
};

async function handleSendMessage() {
    const text = chatInput.value.trim();
    if (!text) return;

    // User Msg
    chatMessages.innerHTML += `
        <div class="flex justify-end">
            <div class="bg-blue-600 text-white rounded-lg rounded-br-none p-3 text-sm shadow-sm max-w-[80%]">${text}</div>
        </div>
    `;
    chatInput.value = '';
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Loading
    const loadingId = 'loading-' + Date.now();
    chatMessages.innerHTML += `
        <div id="${loadingId}" class="flex justify-start">
             <div class="bg-white border border-slate-200 p-3 rounded-lg rounded-bl-none shadow-sm flex items-center space-x-1">
                  <div class="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></div>
                  <div class="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-100"></div>
                  <div class="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-200"></div>
             </div>
        </div>
    `;
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
        const apiKey = process.env.API_KEY;
        if (!apiKey) throw new Error("API Key missing");
        
        const ai = new GoogleGenAI({ apiKey });
        const model = ai.models.getGenerativeModel({ 
            model: "gemini-2.5-flash",
            systemInstruction: "You are 'Sergeant Shingle', the AI virtual assistant for Mil-Spec Roofing. Speak with authority but be helpful. Keep answers concise."
        });
        
        const result = await model.generateContent({ contents: [{ role: 'user', parts: [{ text: text }] }] });
        const response = result.response.text();
        
        document.getElementById(loadingId).remove();
        chatMessages.innerHTML += `
            <div class="flex justify-start">
                <div class="bg-white text-slate-800 border border-slate-200 rounded-lg rounded-bl-none p-3 text-sm shadow-sm max-w-[80%]">${response}</div>
            </div>
        `;
    } catch (e) {
        document.getElementById(loadingId).remove();
        chatMessages.innerHTML += `
            <div class="flex justify-start">
                <div class="bg-red-50 text-red-800 border border-red-200 rounded-lg rounded-bl-none p-3 text-sm shadow-sm max-w-[80%]">Connection to HQ failed. Please call us directly.</div>
            </div>
        `;
    }
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

chatSend.onclick = handleSendMessage;
chatInput.onkeypress = (e) => {
    if (e.key === 'Enter') handleSendMessage();
};
