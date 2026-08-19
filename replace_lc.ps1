$filePath = 'areas-served\league-city\index.html'
$content = [IO.File]::ReadAllText($filePath)

$replacement = @"
    <!-- Roofing Problems in League City -->
    <section class="py-20 bg-white">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto mb-16">
          <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Roofing Problems We See <span class="text-blue-600">in League City</span>
          </h2>
          <div class="h-1 w-20 bg-blue-600 rounded-full mb-6"></div>
          <p class="text-slate-600 text-lg leading-relaxed mb-6">
            League City's proximity to the Gulf Coast means your roof is constantly battling the elements. From torrential downpours and hurricane-force winds to intense Texas UV radiation and coastal humidity, roofs here age differently. Common issues include blown-off shingles, flashing failures around chimneys, and premature granule loss. Ignoring these early warning signs inevitably leads to interior water damage. Whether you need immediate <strong class="font-semibold">roof leak repair league city</strong> homeowners trust, or just routine <strong class="font-semibold">roof maintenance league city</strong> businesses rely on to extend their roof's lifespan, our crews are trained to identify and resolve these specific regional threats.
          </p>
          <a href="/contact-us/" class="inline-block bg-blue-600 text-white font-bold py-3 px-8 rounded hover:bg-blue-700 transition-colors">
            Schedule a Roof Evaluation
          </a>
        </div>

        <!-- Core Services -->
        <div class="max-w-4xl mx-auto">
          <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Comprehensive <span class="text-blue-600">Roofing Services</span>
          </h2>
          <div class="h-1 w-20 bg-blue-600 rounded-full mb-10"></div>

          <div class="space-y-10">
            <!-- Repair -->
            <div>
              <h3 class="text-2xl font-bold text-slate-900 mb-3">Roof Repair</h3>
              <p class="text-slate-600 leading-relaxed">
                When compromised shingles or damaged flashing expose your home to the elements, you need reliable <strong class="font-semibold">roof repair league city</strong> residents can count on. We don't push unnecessary replacements; we pinpoint the exact source of the leak and execute a durable <a href="/services/roof-repair/" class="text-blue-600 hover:underline">roof repair</a> to restore your home's defense against the next storm.
              </p>
            </div>

            <!-- Emergency / Storm -->
            <div>
              <h3 class="text-2xl font-bold text-slate-900 mb-3">Emergency &amp; Storm Damage Roofing</h3>
              <p class="text-slate-600 leading-relaxed">
                After severe Gulf Coast weather, acting fast is critical to prevent secondary water damage. We provide rapid <strong class="font-semibold">emergency roof repair league city</strong> property owners need after high winds or hail. From emergency <a href="/services/roof-tarping/" class="text-blue-600 hover:underline">roof tarping</a> to comprehensive storm damage inspections and insurance claims assistance, we secure your property fast.
              </p>
            </div>

            <!-- Replacement -->
            <div>
              <h3 class="text-2xl font-bold text-slate-900 mb-3">Roof Replacement</h3>
              <p class="text-slate-600 leading-relaxed">
                If your roof has suffered catastrophic damage or reached the end of its natural lifespan, we provide complete tear-offs and <a href="/services/roof-replacement/" class="text-blue-600 hover:underline">roof replacements</a> built to strict windstorm codes. We install high-performance asphalt shingles and impact-resistant materials designed for Texas weather.
              </p>
            </div>

            <!-- Inspection -->
            <div>
              <h3 class="text-2xl font-bold text-slate-900 mb-3">Roof Inspection</h3>
              <p class="text-slate-600 leading-relaxed">
                Before buying, selling, or filing an insurance claim, get the facts. Our comprehensive <a href="/services/roof-inspection/" class="text-blue-600 hover:underline">roof inspections</a> provide a transparent, documented assessment of your roof's health, decking, ventilation, and remaining lifespan.
              </p>
            </div>

            <!-- Res/Com -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 pt-4">
              <div class="bg-slate-50 border border-slate-100 rounded-lg p-6">
                <h4 class="text-xl font-bold text-slate-900 mb-2">Residential Roofing</h4>
                <p class="text-slate-600 text-sm">
                  Your home is your sanctuary. We specialize in <a href="/services/residential-roofing/" class="text-blue-600 hover:underline">residential roofing systems</a> that blend aesthetic appeal with maximum durability, treating your property with the utmost respect from tear-off to final cleanup.
                </p>
              </div>
              <div class="bg-slate-50 border border-slate-100 rounded-lg p-6">
                <h4 class="text-xl font-bold text-slate-900 mb-2">Commercial Roofing</h4>
                <p class="text-slate-600 text-sm">
                  We understand that commercial properties require specialized solutions to minimize operational downtime. We install and repair <a href="/services/commercial-roofing/" class="text-blue-600 hover:underline">flat and low-slope systems</a>, including TPO, EPDM, and Modified Bitumen.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Why Choose Mil-Spec Roofing (Compressed) -->
    <section class="py-16 bg-slate-100">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto text-center">
          <h2 class="text-2xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">Veteran-Owned. Faith-Based. Executed with Precision.</h2>
          <div class="h-1 w-16 bg-blue-600 mx-auto rounded-full mb-6"></div>
          <p class="text-slate-600 leading-relaxed mb-8">
            As a veteran-owned business, Mil-Spec Roofing operates with military discipline—clear communication, attention to detail, and follow-through are standard. We are dedicated to providing the League City community with dependable roofing solutions built on uncompromising workmanship and integrity rooted in faith and service.
          </p>
          <a href="/contact-us/" class="inline-flex items-center text-blue-600 font-bold hover:text-blue-800 transition-colors">
            Contact Our Team <i data-lucide="arrow-right" class="ml-2 w-5 h-5"></i>
          </a>
        </div>
      </div>
    </section>

    <!-- Frequently Asked Questions -->
"@

$newContent = $content -replace '(?is)    <!-- Roof Repair & Replacement -->.*?    <!-- Frequently Asked Questions -->', $replacement
[IO.File]::WriteAllText($filePath, $newContent)
