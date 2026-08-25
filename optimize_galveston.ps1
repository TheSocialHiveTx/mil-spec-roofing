$filePath = "areas-served\galveston\index.html"
$content = [IO.File]::ReadAllText($filePath)

# Update Title and Meta
$content = $content -replace '<title>Roofing Contractor in Galveston, TX \| Mil-Spec Roofing Team</title>', '<title>Top-Rated Galveston Roofing Company &amp; Roofers | Mil-Spec Roofing</title>'
$content = $content -replace 'content="Galveston roofing for coastal wind, salt air, hurricanes, and insurance concerns. Veteran-owned team for repairs, replacements, inspections, and gutters with clear guidance."', 'content="Looking for reliable Galveston roofing companies? Our veteran-owned roofers specialize in storm damage repair, full replacements, and coastal-grade installations."'

# Update Hero H1 and paragraph
$content = $content -replace 'Roofing Services <span class="text-blue-500">in Galveston</span>', 'Expert <span class="text-blue-500">Galveston Roofing Company</span> &amp; Contractors'
$content = $content -replace 'Built to protect what matters most. From inspections to replacements, Mil-Spec Roofing delivers durable.*?results with discipline, integrity, and respect for your home or business.', 'Built to protect what matters most. As one of the premier roofing companies in Galveston, TX, we deliver marine-grade durability, storm damage restoration, and uncompromising military discipline for your home or business.'

# Replace the "About + Who We Are" section up to "Our Galveston Process"
$newSection = @"
    <!-- Galveston Roofing Company Authority -->
    <section class="py-20 bg-white border-b border-slate-200">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto mb-16 text-center">
          <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Your Trusted <span class="text-blue-600">Galveston Roofing Company</span>
          </h2>
          <div class="h-1 w-20 bg-blue-600 mx-auto rounded-full mb-6"></div>
          <p class="text-slate-600 text-lg leading-relaxed mb-6">
            When island weather puts your property to the test, you need <strong class="font-bold text-slate-800">roofers in Galveston</strong> who understand coastal dynamics. From intense salt-air corrosion and hurricane-force winds to sudden hail storms, our veteran-owned team engineers roofing systems that survive the Gulf Coast. Whether you're searching for <strong class="font-bold text-slate-800">roofing contractors in Galveston</strong> to handle a complex commercial flat roof, or simply need an honest residential inspection after a severe squall, Mil-Spec Roofing delivers military-grade precision and uncompromised integrity.
          </p>
        </div>

        <!-- Galveston Roofing Services Grid -->
        <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          
          <!-- Storm Damage (Strong Intent) -->
          <div class="bg-blue-50 p-8 rounded-xl border border-blue-100 shadow-sm hover:shadow-md transition-shadow">
            <h3 class="text-2xl font-bold text-slate-900 mb-3"><a href="/services/emergency-roofing/" class="hover:text-blue-600">Storm &amp; Wind Damage Repair</a></h3>
            <p class="text-slate-600 leading-relaxed mb-4">
              Galveston's weather is notoriously aggressive. We dominate in <a href="/services/roof-tarping/" class="text-blue-600 font-semibold hover:underline">wind damage roof repair</a> and <a href="/services/roof-repair/" class="text-blue-600 font-semibold hover:underline">hail damage restoration</a>. From emergency tarping to insurance claims assistance, we secure your property immediately after the storm passes.
            </p>
          </div>

          <!-- Roof Repair -->
          <div class="bg-white p-8 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
            <h3 class="text-2xl font-bold text-slate-900 mb-3"><a href="/services/roof-repair/" class="hover:text-blue-600">Targeted Roof Repair</a></h3>
            <p class="text-slate-600 leading-relaxed mb-4">
              Not every issue requires a total overhaul. As highly ethical <a href="/services/roof-repair/" class="text-blue-600 font-semibold hover:underline">Galveston roofers</a>, we surgically repair flashing failures, wind-lifted shingles, and coastal-driven leaks to maximize your roof's remaining lifespan.
            </p>
          </div>

          <!-- Roof Replacement -->
          <div class="bg-white p-8 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
            <h3 class="text-2xl font-bold text-slate-900 mb-3"><a href="/services/roof-replacement/" class="hover:text-blue-600">Full Roof Replacement</a></h3>
            <p class="text-slate-600 leading-relaxed mb-4">
              When salt air and time have compromised your decking, we execute complete <a href="/services/roof-replacement/" class="text-blue-600 font-semibold hover:underline">roof replacements</a>. We install windstorm-certified, marine-grade systems built explicitly for the island's extreme demands.
            </p>
          </div>

          <!-- Residential -->
          <div class="bg-white p-8 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
            <h3 class="text-2xl font-bold text-slate-900 mb-3"><a href="/services/residential-roofing/" class="hover:text-blue-600">Residential Roofing</a></h3>
            <p class="text-slate-600 leading-relaxed mb-4">
              Protecting island families is our priority. We offer <a href="/services/residential-roofing/" class="text-blue-600 font-semibold hover:underline">residential roofing</a> solutions featuring impact-resistant architectural shingles and enhanced underlayments designed to reject moisture and high winds.
            </p>
          </div>

          <!-- Commercial -->
          <div class="bg-white p-8 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
            <h3 class="text-2xl font-bold text-slate-900 mb-3"><a href="/services/commercial-roofing/" class="hover:text-blue-600">Commercial &amp; Flat Roofing</a></h3>
            <p class="text-slate-600 leading-relaxed mb-4">
              Unlike many generic <strong class="font-bold text-slate-700">Galveston roofing companies</strong>, we specialize in high-performance <a href="/services/commercial-roofing/" class="text-blue-600 font-semibold hover:underline">commercial flat roofing</a> (TPO, EPDM, Modified Bitumen) engineered to withstand heavy coastal rains and UV degradation.
            </p>
          </div>

          <!-- Inspection -->
          <div class="bg-white p-8 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
            <h3 class="text-2xl font-bold text-slate-900 mb-3"><a href="/services/roof-inspection/" class="hover:text-blue-600">Coastal Roof Inspections</a></h3>
            <p class="text-slate-600 leading-relaxed mb-4">
              Whether required for insurance, real estate transactions, or post-hurricane peace of mind, our comprehensive <a href="/services/roof-inspection/" class="text-blue-600 font-semibold hover:underline">roof inspections</a> provide fully documented proof of your roof's integrity.
            </p>
          </div>

        </div>
      </div>
    </section>

    <!-- Our Galveston Process -->
"@

$content = $content -replace '(?is)    <!-- About \+ Who We Are \(same spacing, new copy\) -->.*?    <!-- Our Galveston Process -->', $newSection

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
