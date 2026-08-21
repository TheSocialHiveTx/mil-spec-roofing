$filePath = "areas-served\league-city\index.html"
$content = [IO.File]::ReadAllText($filePath)

$newSection = @"
    <!-- Featured League City Project -->
    <section class="py-20 bg-white border-b border-slate-200">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Featured <span class="text-blue-600">League City</span> Project
          </h2>
          <div class="h-1 w-20 bg-blue-600 mx-auto rounded-full mb-8"></div>
        </div>

        <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
          
          <!-- Project Details -->
          <div class="lg:col-span-7">
            <h3 class="text-2xl md:text-3xl font-bold text-slate-900 mb-6 uppercase tracking-tight">Residential Roof Replacement &amp; Exterior Repairs</h3>
            
            <p class="text-slate-600 text-lg leading-relaxed mb-5">
              Mil-Spec Roofing &amp; Construction completed a full residential roof replacement for a homeowner who wanted to ensure his home was properly protected and maintained for his family. With personal health concerns in mind, his priority was addressing the roof and other exterior issues now so his wife would not be left dealing with major home repairs in the future.
            </p>
            
            <p class="text-slate-600 text-lg leading-relaxed mb-5">
              The project included removal of the existing roofing system and installation of a new architectural shingle roof. We also replaced the roof vents to improve ventilation and ensure the new roofing system was properly finished around each penetration.
            </p>
            
            <p class="text-slate-600 text-lg leading-relaxed mb-8">
              While completing the exterior work, we addressed termite damage affecting the home's front porch columns. The damaged columns were rebuilt to restore the structure and provide a clean, finished appearance that complemented the new roof.
            </p>
            
            <h4 class="text-xl font-bold text-slate-900 mb-4 uppercase tracking-tight border-l-4 border-blue-600 pl-3">Work Completed</h4>
            <ul class="space-y-3 mb-8">
              <li class="flex items-start">
                <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                <span class="text-slate-700 font-medium">Complete residential roof replacement</span>
              </li>
              <li class="flex items-start">
                <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                <span class="text-slate-700 font-medium">Architectural shingle installation</span>
              </li>
              <li class="flex items-start">
                <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                <span class="text-slate-700 font-medium">New roof vents</span>
              </li>
              <li class="flex items-start">
                <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                <span class="text-slate-700 font-medium">Roofing ventilation and penetration detailing</span>
              </li>
              <li class="flex items-start">
                <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                <span class="text-slate-700 font-medium">Removal and replacement of termite-damaged porch components</span>
              </li>
              <li class="flex items-start">
                <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                <span class="text-slate-700 font-medium">Front porch column reconstruction</span>
              </li>
              <li class="flex items-start">
                <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mr-3 flex-shrink-0"></i>
                <span class="text-slate-700 font-medium">Exterior construction and repairs</span>
              </li>
            </ul>

            <div class="bg-blue-50/50 p-6 rounded-xl border border-blue-100">
              <p class="text-slate-700 leading-relaxed font-medium italic">
                This project demonstrates Mil-Spec Roofing &amp; Construction's ability to handle both <strong class="font-bold text-blue-900">residential roofing and exterior construction</strong> as part of a complete home improvement project. By addressing the roof, ventilation, and damaged porch columns together, the homeowner was able to leave the property in better condition and gain confidence that the major exterior issues had been properly addressed.
              </p>
            </div>
            
            <div class="mt-8">
              <a href="/contact-us/" class="inline-flex items-center text-white bg-blue-600 font-bold px-8 py-4 rounded hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl">
                Get a Quote for Your Home <i data-lucide="arrow-right" class="ml-2 w-5 h-5"></i>
              </a>
            </div>
          </div>

          <!-- Project Gallery Grid -->
          <div class="lg:col-span-5 grid grid-cols-2 gap-4">
            <a href="/images/league-city-roof-replacement-after-storm.jpg" target="_blank" class="block overflow-hidden rounded-xl shadow-sm hover:shadow-md transition-shadow group">
              <img src="/images/league-city-roof-replacement-after-storm.jpg" alt="League City residential roof replacement" class="w-full h-40 object-cover transform group-hover:scale-110 transition-transform duration-500" loading="lazy">
            </a>
            <a href="/images/league-city-residential-roofing-project.jpg" target="_blank" class="block overflow-hidden rounded-xl shadow-sm hover:shadow-md transition-shadow group">
              <img src="/images/league-city-residential-roofing-project.jpg" alt="New architectural shingle roof installed in League City" class="w-full h-40 object-cover transform group-hover:scale-110 transition-transform duration-500" loading="lazy">
            </a>
            <a href="/images/windstorm-certified-roof-league-city.jpg" target="_blank" class="block overflow-hidden rounded-xl shadow-sm hover:shadow-md transition-shadow group col-span-2">
              <img src="/images/windstorm-certified-roof-league-city.jpg" alt="Roofing ventilation and penetration detailing" class="w-full h-56 object-cover transform group-hover:scale-110 transition-transform duration-500" loading="lazy">
            </a>
            <a href="/images/league-city-roof-inspection-results.jpg" target="_blank" class="block overflow-hidden rounded-xl shadow-sm hover:shadow-md transition-shadow group">
              <img src="/images/league-city-roof-inspection-results.jpg" alt="Front porch column reconstruction and exterior repairs" class="w-full h-40 object-cover transform group-hover:scale-110 transition-transform duration-500" loading="lazy">
            </a>
            <a href="/images/emergency-roof-repair-league-city-tx.jpg" target="_blank" class="block overflow-hidden rounded-xl shadow-sm hover:shadow-md transition-shadow group">
              <img src="/images/emergency-roof-repair-league-city-tx.jpg" alt="Termite-damaged porch components replaced in League City" class="w-full h-40 object-cover transform group-hover:scale-110 transition-transform duration-500" loading="lazy">
            </a>
            <a href="/images/league-city-commercial-roofing-work.jpg" target="_blank" class="block overflow-hidden rounded-xl shadow-sm hover:shadow-md transition-shadow group col-span-2">
              <img src="/images/league-city-commercial-roofing-work.jpg" alt="Finished complete home improvement project exterior" class="w-full h-56 object-cover transform group-hover:scale-110 transition-transform duration-500" loading="lazy">
            </a>
          </div>
          
        </div>
      </div>
    </section>

    <!-- Frequently Asked Questions -->
"@

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$content = $content -replace '(?is)    <!-- Recent League City Roofing Work -->.*?    <!-- Frequently Asked Questions -->', $newSection
[IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
