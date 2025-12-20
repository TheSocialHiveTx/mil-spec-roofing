
import React, { useState, useEffect } from 'react';
import { NAV_ITEMS, SERVICES, CONSTRUCTION_FEATURES } from './constants';
import Assistant from './components/Assistant';

const App: React.FC = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className="min-h-screen">
      {/* Navigation */}
      <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${isScrolled ? 'glass-morphism shadow-md py-3' : 'bg-transparent py-6'}`}>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="bg-slate-900 text-white p-2 rounded font-black text-xl tracking-tighter">MIL-SPEC</div>
            <div className="hidden md:block font-bold text-slate-800 uppercase tracking-widest text-xs">Roofing & Construction</div>
          </div>
          
          <div className="hidden md:flex items-center gap-8">
            {NAV_ITEMS.map((item) => (
              <a 
                key={item.href} 
                href={item.href} 
                className="text-sm font-semibold text-slate-600 hover:text-blue-600 transition-colors uppercase tracking-wider"
              >
                {item.label}
              </a>
            ))}
            <a 
              href="#contact" 
              className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2.5 rounded-full text-sm font-bold transition-all transform hover:scale-105"
            >
              Get a Quote
            </a>
          </div>

          <button onClick={() => setMobileMenuOpen(!mobileMenuOpen)} className="md:hidden p-2 text-slate-800">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d={mobileMenuOpen ? "M6 18L18 6M6 6l12 12" : "M4 6h16M4 12h16M4 18h16"} />
            </svg>
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden glass-morphism border-t border-slate-200 absolute top-full left-0 right-0 p-4 space-y-4 shadow-xl">
            {NAV_ITEMS.map((item) => (
              <a 
                key={item.href} 
                href={item.href} 
                onClick={() => setMobileMenuOpen(false)}
                className="block text-lg font-bold text-slate-800 py-2 border-b border-slate-100"
              >
                {item.label}
              </a>
            ))}
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section id="home" className="relative h-screen flex items-center overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img 
            src="https://picsum.photos/seed/construction-main/1920/1080" 
            className="w-full h-full object-cover brightness-[0.4]" 
            alt="Construction background"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-slate-950/80 to-transparent"></div>
        </div>
        
        <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 bg-blue-600/20 border border-blue-500/30 px-4 py-1.5 rounded-full text-blue-400 font-bold text-xs uppercase tracking-widest mb-8">
              <span className="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></span>
              Veteran Owned & Operated
            </div>
            <h1 className="text-5xl md:text-7xl lg:text-8xl font-black text-white leading-tight tracking-tighter mb-6">
              BUILT TO <br/><span className="text-blue-500 italic">LAST.</span>
            </h1>
            <p className="text-lg md:text-xl text-slate-300 mb-10 leading-relaxed font-medium max-w-xl">
              From precision roofing to full-scale general construction, we bring military discipline and elite craftsmanship to every project.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <a href="#construction" className="bg-white text-slate-950 px-10 py-4 rounded-full font-black text-lg hover:bg-blue-600 hover:text-white transition-all text-center">
                Our Services
              </a>
              <a href="#contact" className="border-2 border-white/30 text-white px-10 py-4 rounded-full font-black text-lg hover:bg-white/10 transition-all text-center">
                Contact Us
              </a>
            </div>
          </div>
        </div>

        <div className="absolute bottom-10 left-1/2 -translate-x-1/2 animate-bounce hidden md:block">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 text-white/50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
          </svg>
        </div>
      </section>

      {/* Services Section */}
      <section id="construction" className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
            <div className="max-w-2xl">
              <h2 className="text-slate-900 text-4xl md:text-5xl font-black tracking-tighter mb-4">GENERAL CONSTRUCTION</h2>
              <div className="h-1.5 w-24 bg-blue-600 rounded-full mb-6"></div>
              <p className="text-slate-600 text-lg font-medium">
                We handle every aspect of your building project. Our "Mil-Spec" standard ensures zero defects and lasting structural integrity.
              </p>
            </div>
            <div className="flex gap-2">
               <button className="p-3 rounded-full border border-slate-200 hover:bg-slate-50 transition-colors">
                 <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" /></svg>
               </button>
               <button className="p-3 rounded-full bg-slate-900 text-white hover:bg-slate-800 transition-colors">
                 <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" /></svg>
               </button>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {SERVICES.map((service) => (
              <div key={service.id} className="group cursor-pointer">
                <div className="relative overflow-hidden rounded-3xl aspect-[4/5] mb-6">
                  <img 
                    src={service.image} 
                    alt={service.title} 
                    className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent opacity-60 group-hover:opacity-80 transition-opacity"></div>
                  <div className="absolute top-6 left-6 text-4xl">{service.icon}</div>
                  <div className="absolute bottom-8 left-8 right-8">
                    <h3 className="text-white text-2xl font-black mb-2">{service.title}</h3>
                    <p className="text-slate-300 text-sm line-clamp-2 group-hover:line-clamp-none transition-all duration-300">{service.description}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="mt-20 bg-slate-50 rounded-[3rem] p-12 md:p-20 overflow-hidden relative">
            <div className="absolute top-0 right-0 p-10 opacity-5 pointer-events-none hidden lg:block">
              <svg className="w-96 h-96" viewBox="0 0 100 100" fill="currentColor"><circle cx="50" cy="50" r="40" /></svg>
            </div>
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
              <div>
                <h3 className="text-3xl font-black text-slate-900 mb-8 uppercase tracking-tight italic">Our Capabilities</h3>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-y-4 gap-x-8">
                  {CONSTRUCTION_FEATURES.map((feature, idx) => (
                    <div key={idx} className="flex items-center gap-3">
                      <div className="flex-shrink-0 w-6 h-6 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                          <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                        </svg>
                      </div>
                      <span className="text-slate-700 font-semibold">{feature}</span>
                    </div>
                  ))}
                </div>
              </div>
              <div className="bg-white p-8 rounded-3xl shadow-xl border border-slate-100">
                <h4 className="text-xl font-bold text-slate-900 mb-4">Request a Consultation</h4>
                <p className="text-slate-500 text-sm mb-6">Schedule a free on-site assessment with our project managers.</p>
                <form className="space-y-4">
                  <input type="text" placeholder="Full Name" className="w-full bg-slate-50 border-none rounded-xl px-5 py-3 focus:ring-2 focus:ring-blue-500 outline-none" />
                  <input type="email" placeholder="Email Address" className="w-full bg-slate-50 border-none rounded-xl px-5 py-3 focus:ring-2 focus:ring-blue-500 outline-none" />
                  <textarea placeholder="Tell us about your project..." rows={3} className="w-full bg-slate-50 border-none rounded-xl px-5 py-3 focus:ring-2 focus:ring-blue-500 outline-none"></textarea>
                  <button className="w-full bg-slate-900 text-white font-black py-4 rounded-xl hover:bg-blue-600 transition-colors uppercase tracking-widest text-sm">Send Request</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="bg-slate-950 py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-2 md:grid-cols-4 gap-12 text-center">
          <div>
            <div className="text-5xl font-black text-white mb-2 italic tracking-tighter">15+</div>
            <div className="text-blue-500 text-xs font-bold uppercase tracking-widest">Years Experience</div>
          </div>
          <div>
            <div className="text-5xl font-black text-white mb-2 italic tracking-tighter">1.2k</div>
            <div className="text-blue-500 text-xs font-bold uppercase tracking-widest">Projects Completed</div>
          </div>
          <div>
            <div className="text-5xl font-black text-white mb-2 italic tracking-tighter">100%</div>
            <div className="text-blue-500 text-xs font-bold uppercase tracking-widest">Veteran Staff</div>
          </div>
          <div>
            <div className="text-5xl font-black text-white mb-2 italic tracking-tighter">A+</div>
            <div className="text-blue-500 text-xs font-bold uppercase tracking-widest">BBB Rated</div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-white border-t border-slate-100 py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
            <div className="col-span-1 md:col-span-2">
               <div className="bg-slate-900 text-white inline-block p-2 rounded font-black text-xl tracking-tighter mb-6">MIL-SPEC</div>
               <p className="text-slate-500 max-w-sm mb-8 font-medium">
                 Elite roofing and construction services for residential and commercial clients. We don't just build, we fortify.
               </p>
               <div className="flex gap-4">
                 {['fb', 'tw', 'ig', 'li'].map(social => (
                   <div key={social} className="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center cursor-pointer hover:bg-blue-600 hover:text-white transition-all">
                     <span className="uppercase text-xs font-bold">{social}</span>
                   </div>
                 ))}
               </div>
            </div>
            <div>
              <h4 className="font-black text-slate-900 mb-6 uppercase tracking-wider text-sm">Services</h4>
              <ul className="space-y-3 text-slate-500 font-semibold text-sm">
                <li><a href="#" className="hover:text-blue-600">Roof Replacement</a></li>
                <li><a href="#" className="hover:text-blue-600">Storm Damage Repair</a></li>
                <li><a href="#" className="hover:text-blue-600">Kitchen Remodeling</a></li>
                <li><a href="#" className="hover:text-blue-600">Custom Decks</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-black text-slate-900 mb-6 uppercase tracking-wider text-sm">Company</h4>
              <ul className="space-y-3 text-slate-500 font-semibold text-sm">
                <li><a href="#" className="hover:text-blue-600">About Us</a></li>
                <li><a href="#" className="hover:text-blue-600">Our Mission</a></li>
                <li><a href="#" className="hover:text-blue-600">Careers</a></li>
                <li><a href="#" className="hover:text-blue-600">Contact</a></li>
              </ul>
            </div>
          </div>
          <div className="pt-12 border-t border-slate-100 flex flex-col md:row items-center justify-between gap-6 text-slate-400 text-xs font-bold uppercase tracking-widest">
            <p>© 2024 MIL-SPEC ROOFING & CONSTRUCTION. ALL RIGHTS RESERVED.</p>
            <div className="flex gap-8">
              <a href="#" className="hover:text-slate-600">Privacy Policy</a>
              <a href="#" className="hover:text-slate-600">Terms of Service</a>
            </div>
          </div>
        </div>
      </footer>

      {/* AI Consultant Component */}
      <Assistant />
    </div>
  );
};

export default App;
