$filePath = "areas-served\galveston\index.html"
$content = [IO.File]::ReadAllText($filePath)

$newSection = @"
    <!-- Featured Galveston Coastal Project -->
    <section class="py-20 bg-slate-50 border-b border-slate-200">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Featured <span class="text-blue-600">Galveston</span> Coastal Project
          </h2>
          <div class="h-1 w-20 bg-blue-600 mx-auto rounded-full mb-8"></div>
        </div>

        <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
          
          <!-- Project Details -->
          <div class="lg:col-span-7">
            <h3 class="text-2xl md:text-3xl font-bold text-slate-900 mb-6 uppercase tracking-tight">Residential Roof Replacement in Galveston, TX</h3>
            
            <p class="text-slate-600 text-lg leading-relaxed mb-5">
              Mil-Spec Roofing &amp; Construction completed a full residential roof replacement on this coastal home in Galveston, Texas. The project included removal of the existing roofing system, inspection and preparation of the exposed roof decking, and installation of a new CertainTeed asphalt shingle roofing system.
            </p>
            
            <p class="text-slate-600 text-lg leading-relaxed mb-8">
              Roofing in Galveston requires careful consideration of the Texas Gulf Coast environment. Homes in the area are regularly exposed to strong coastal winds, wind-driven rain, intense sunlight, high humidity, and salt air. For this project, CertainTeed roofing products were used to provide a durable, professionally installed roofing system suited for the demands of a coastal residential property.
            </p>
            
            <div class="bg-white p-6 rounded-xl border border-slate-200 mb-8 shadow-sm">
              <h4 class="text-xl font-bold text-slate-900 mb-4 uppercase tracking-tight border-l-4 border-blue-600 pl-3">Project Details</h4>
              <ul class="space-y-3">
                <li class="flex items-start">
                  <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                  <div><strong class="text-slate-900">Location:</strong> <span class="text-slate-700 font-medium">Galveston, TX</span></div>
                </li>
                <li class="flex items-start">
                  <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                  <div><strong class="text-slate-900">Service:</strong> <span class="text-slate-700 font-medium">Complete Residential Roof Replacement</span></div>
                </li>
                <li class="flex items-start">
                  <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                  <div><strong class="text-slate-900">Property Type:</strong> <span class="text-slate-700 font-medium">Coastal Residential Home</span></div>
                </li>
                <li class="flex items-start">
                  <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                  <div><strong class="text-slate-900">Manufacturer:</strong> <span class="text-slate-700 font-medium">CertainTeed</span></div>
                </li>
                <li class="flex items-start">
                  <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                  <div><strong class="text-slate-900">Material:</strong> <span class="text-slate-700 font-medium">Asphalt Shingles</span></div>
                </li>
                <li class="flex items-start">
                  <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                  <div><strong class="text-slate-900">Work Performed:</strong> <span class="text-slate-700 font-medium">Roof tear-off, roof deck inspection and preparation, and new roofing system installation</span></div>
                </li>
              </ul>
            </div>

            <div class="bg-blue-50/50 p-6 rounded-xl border border-blue-100 mb-8">
              <p class="text-slate-700 leading-relaxed font-medium italic">
                From the initial tear-off through final installation, Mil-Spec Roofing &amp; Construction completed the project with attention to proper installation, weather protection, and long-term roof performance.
              </p>
              <p class="text-slate-700 leading-relaxed font-medium italic mt-4">
                Mil-Spec Roofing &amp; Construction provides <strong class="font-bold text-blue-900"><a href="/services/roof-replacement/">roof replacement</a>, <a href="/services/roof-repair/">roof repair</a>, and <a href="/services/residential-roofing/">residential roofing services</a> in Galveston, TX</strong> and throughout the surrounding Texas Gulf Coast communities.
              </p>
            </div>
            
            <div class="mt-8">
              <a href="/contact-us/" class="inline-flex items-center text-white bg-blue-600 font-bold px-8 py-4 rounded hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl">
                Get a Quote for Your Coastal Home <i data-lucide="arrow-right" class="ml-2 w-5 h-5"></i>
              </a>
            </div>
          </div>

          <!-- Project Gallery Grid -->
          <div class="lg:col-span-5 flex flex-col gap-6">
            <a href="/images/galveston-tx-residential-roof-replacement-certainteed-asphalt.png" target="_blank" class="block overflow-hidden rounded-xl shadow-sm hover:shadow-md transition-shadow group">
              <img src="/images/galveston-tx-residential-roof-replacement-certainteed-asphalt.png" alt="Galveston TX residential roof replacement using CertainTeed asphalt shingles" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
            </a>
            <a href="/images/galveston-roof-deck-inspection-coastal-preparation.png" target="_blank" class="block overflow-hidden rounded-xl shadow-sm hover:shadow-md transition-shadow group">
              <img src="/images/galveston-roof-deck-inspection-coastal-preparation.png" alt="Roof tear-off, roof deck inspection, and preparation for a Galveston coastal home" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
            </a>
            <a href="/images/galveston-coastal-roofing-contractor-new-shingle-installation.png" target="_blank" class="block overflow-hidden rounded-xl shadow-sm hover:shadow-md transition-shadow group">
              <img src="/images/galveston-coastal-roofing-contractor-new-shingle-installation.png" alt="New CertainTeed roofing system installation by Mil-Spec Roofing in Galveston TX" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
            </a>
          </div>
          
        </div>
      </div>
    </section>

    <!-- Our Galveston Process -->
"@

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$content = $content -replace '(?is)    <!-- Our Galveston Process -->', $newSection
[IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
