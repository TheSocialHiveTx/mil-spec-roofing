$filePath = "areas-served\league-city\index.html"
$content = [IO.File]::ReadAllText($filePath)

$newSection = @"
    <!-- Recent League City Roofing Work -->
    <section class="py-20 bg-white border-b border-slate-200">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Recent <span class="text-blue-600">League City</span> Roofing Work
          </h2>
          <div class="h-1 w-20 bg-blue-600 mx-auto rounded-full mb-6"></div>
          <p class="text-slate-600 text-lg max-w-2xl mx-auto">
            Visual proof of our commitment to quality. Here are verified projects we've recently completed in League City, built to withstand the toughest Gulf Coast conditions.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
          <!-- Project 1 -->
          <a href="/services/roof-replacement/" class="group block relative rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all">
            <img src="/images/league-city-roof-replacement-after-storm.jpg" alt="Windstorm-certified asphalt shingle roof replacement after severe storm damage in League City, TX" class="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent opacity-80 group-hover:opacity-90 transition-opacity"></div>
            <div class="absolute bottom-0 left-0 p-6">
              <span class="text-blue-400 text-xs font-bold uppercase tracking-wider mb-1 block">Roof Replacement</span>
              <h3 class="text-white text-lg font-bold">Storm Damage Restoration</h3>
            </div>
          </a>
          
          <!-- Project 2 -->
          <a href="/services/residential-roofing/" class="group block relative rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all">
            <img src="/images/league-city-residential-roofing-project.jpg" alt="Completed residential roofing project in a League City neighborhood showing new architectural shingles" class="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent opacity-80 group-hover:opacity-90 transition-opacity"></div>
            <div class="absolute bottom-0 left-0 p-6">
              <span class="text-blue-400 text-xs font-bold uppercase tracking-wider mb-1 block">Residential Roofing</span>
              <h3 class="text-white text-lg font-bold">Architectural Shingle Upgrade</h3>
            </div>
          </a>

          <!-- Project 3 -->
          <a href="/services/roof-inspection/" class="group block relative rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all">
            <img src="/images/windstorm-certified-roof-league-city.jpg" alt="Mil-Spec Roofing performing a windstorm-certified roof installation and inspection in League City" class="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent opacity-80 group-hover:opacity-90 transition-opacity"></div>
            <div class="absolute bottom-0 left-0 p-6">
              <span class="text-blue-400 text-xs font-bold uppercase tracking-wider mb-1 block">Windstorm Certified</span>
              <h3 class="text-white text-lg font-bold">Code-Compliant Installation</h3>
            </div>
          </a>

          <!-- Project 4 -->
          <a href="/services/emergency-roofing/" class="group block relative rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all">
            <img src="/images/emergency-roof-repair-league-city-tx.jpg" alt="Emergency roof repair and tarping services provided to a League City homeowner after high winds" class="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent opacity-80 group-hover:opacity-90 transition-opacity"></div>
            <div class="absolute bottom-0 left-0 p-6">
              <span class="text-blue-400 text-xs font-bold uppercase tracking-wider mb-1 block">Emergency Repair</span>
              <h3 class="text-white text-lg font-bold">Rapid Storm Response</h3>
            </div>
          </a>

          <!-- Project 5 -->
          <a href="/services/commercial-roofing/" class="group block relative rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all">
            <img src="/images/league-city-commercial-roofing-work.jpg" alt="Commercial flat roofing project completed for a business in League City, TX" class="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent opacity-80 group-hover:opacity-90 transition-opacity"></div>
            <div class="absolute bottom-0 left-0 p-6">
              <span class="text-blue-400 text-xs font-bold uppercase tracking-wider mb-1 block">Commercial Roofing</span>
              <h3 class="text-white text-lg font-bold">Flat Roof System</h3>
            </div>
          </a>

          <!-- Project 6 -->
          <a href="/project-gallery/" class="group block relative rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all">
            <img src="/images/league-city-roofing-contractor-project.jpg" alt="Final walkthrough of a completed roof replacement by Mil-Spec Roofing in League City" class="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500" loading="lazy">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent opacity-80 group-hover:opacity-90 transition-opacity"></div>
            <div class="absolute bottom-0 left-0 p-6">
              <span class="text-blue-400 text-xs font-bold uppercase tracking-wider mb-1 block">Project Gallery</span>
              <h3 class="text-white text-lg font-bold">Final Quality Inspection</h3>
            </div>
          </a>
        </div>
        
        <div class="text-center mt-12">
          <a href="/project-gallery/" class="inline-flex items-center text-blue-600 font-bold hover:text-blue-800 transition-colors border border-blue-200 px-6 py-3 rounded hover:bg-blue-50">
            View Full Project Gallery <i data-lucide="arrow-right" class="ml-2 w-5 h-5"></i>
          </a>
        </div>
      </div>
    </section>

    <!-- Frequently Asked Questions -->
"@

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$content = $content -replace '    <!-- Frequently Asked Questions -->', $newSection
[IO.File]::WriteAllText($filePath, $content, $utf8NoBom)

# Delete old pics folder
Remove-Item -Recurse -Force "leaguecitypics"
