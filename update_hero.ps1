$filePath = "index.html"
$content = [IO.File]::ReadAllText($filePath)

$newHero = @"
        <section id="home" class="relative min-h-[700px] flex items-center justify-center overflow-hidden bg-slate-900 pb-16 pt-32 md:pt-40">
            <div class="absolute inset-0 z-0">
                <img src="/images/mil-specroof5.JPG" alt="Mil-Spec Roofing Project"
                    class="w-full h-full object-cover opacity-40" loading="lazy" />
                <div class="absolute inset-0 bg-gradient-to-r from-slate-950 via-slate-900/95 to-slate-900/50"></div>
            </div>

            <div class="container mx-auto px-4 relative z-10 flex flex-col lg:flex-row items-center gap-12">
                <!-- Left Side Text -->
                <div class="w-full lg:w-1/2 text-white text-center lg:text-left pt-8">
                    <div class="inline-flex items-center justify-center space-x-2 bg-slate-800/80 border border-slate-700 rounded-full px-5 py-2 mb-6 backdrop-blur-sm">
                        <i data-lucide="shield-check" class="text-blue-400 h-5 w-5"></i>
                        <span class="text-slate-200 text-sm font-semibold tracking-wide">Veteran Owned & Operated</span>
                    </div>

                    <h2 class="text-blue-400 text-xl md:text-2xl font-bold uppercase tracking-wide mb-2 drop-shadow">
                        Mil-Spec Roofing & Construction
                    </h2>
                    
                    <h1 class="text-5xl md:text-6xl lg:text-[4.5rem] font-extrabold leading-[1.05] mb-6 drop-shadow-xl uppercase tracking-tight">
                        We Protect <br class="hidden md:block">
                        <span class="text-blue-400">The Core Systems</span> <br class="hidden md:block">
                        To Keep Your <br class="hidden md:block">
                        Home Running
                    </h1>

                    <p class="text-lg md:text-xl text-slate-300 mb-8 max-w-xl mx-auto lg:mx-0 leading-relaxed">
                        Mil-Spec Roofing delivers dependable roof repair, roof replacement, and storm damage 
inspections for homeowners and businesses across Southeast Texas. Our approach emphasizes precision, accountability, and doing the job right the first time.
                    </p>
                </div>

                <!-- Right Side Form -->
                <div class="w-full lg:w-1/2 flex justify-center lg:justify-end">
                    <div class="bg-white rounded-2xl shadow-2xl p-6 md:p-8 w-full max-w-lg text-slate-900 relative z-20">
                        <h3 class="text-2xl font-bold text-slate-900 mb-2">Schedule your free inspection</h3>
                        <p class="text-slate-500 mb-6 text-sm">Fill out the form below and we'll be in touch shortly.</p>
                        
                        <form action="/contact-us/" method="POST" class="space-y-4">
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-sm font-semibold text-slate-700 mb-1">First Name</label>
                                    <input type="text" placeholder="John" class="w-full border border-slate-200 rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all">
                                </div>
                                <div>
                                    <label class="block text-sm font-semibold text-slate-700 mb-1">Last Name</label>
                                    <input type="text" placeholder="Doe" class="w-full border border-slate-200 rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all">
                                </div>
                            </div>

                            <div>
                                <label class="block text-sm font-semibold text-slate-700 mb-1">Phone <span class="text-red-500">*</span></label>
                                <input type="tel" placeholder="(832) 555-0123" required class="w-full border border-slate-200 rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all">
                            </div>

                            <div>
                                <label class="block text-sm font-semibold text-slate-700 mb-1">Address</label>
                                <input type="text" placeholder="Enter your full address" class="w-full border border-slate-200 rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all">
                            </div>

                            <div>
                                <label class="block text-sm font-semibold text-slate-700 mb-1">Service Needed</label>
                                <div class="relative">
                                    <select class="w-full border border-slate-200 rounded-lg px-4 py-2.5 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all appearance-none pr-10">
                                        <option>Roofing</option>
                                        <option>Gutters & Siding</option>
                                        <option>Storm Damage Inspection</option>
                                        <option>General Construction</option>
                                        <option>Other</option>
                                    </select>
                                    <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3 text-slate-500">
                                        <svg class="h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"/></svg>
                                    </div>
                                </div>
                            </div>

                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-sm font-semibold text-slate-700 mb-1">Preferred Date</label>
                                    <input type="date" class="w-full border border-slate-200 rounded-lg px-4 py-2.5 text-slate-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all">
                                </div>
                                <div>
                                    <label class="block text-sm font-semibold text-slate-700 mb-1">Preferred Time</label>
                                    <div class="relative">
                                        <select class="w-full border border-slate-200 rounded-lg px-4 py-2.5 bg-white text-slate-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all appearance-none pr-10">
                                            <option>Select time slot</option>
                                            <option>Morning (8am - 12pm)</option>
                                            <option>Afternoon (12pm - 4pm)</option>
                                            <option>Evening (4pm - 6pm)</option>
                                        </select>
                                        <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3 text-slate-500">
                                            <svg class="h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"/></svg>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3.5 px-4 rounded-lg transition-colors mt-4">
                                Request Free Inspection
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </section>
"@

$content = $content -replace '(?is)<section id="home".*?</section>', $newHero

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
