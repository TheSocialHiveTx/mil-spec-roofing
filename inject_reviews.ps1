$filePath = "areas-served\league-city\index.html"
$content = [IO.File]::ReadAllText($filePath)

$reviewsSection = @"
    <!-- League City Verified Reviews -->
    <section class="py-16 bg-slate-50 border-b border-slate-200">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-extrabold text-slate-900 mb-4 uppercase tracking-tight">
            Trusted by <span class="text-blue-600">League City</span> Homeowners
          </h2>
          <div class="h-1 w-20 bg-blue-600 mx-auto rounded-full mb-6"></div>
        </div>
        
        <div class="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
          <!-- Review 1 -->
          <div class="bg-white p-8 rounded-xl shadow-md border border-slate-100 flex flex-col h-full relative group hover:shadow-lg transition-shadow">
            <div class="absolute top-6 right-6 text-blue-50 transform rotate-180 pointer-events-none group-hover:text-blue-100 transition-colors">
              <i data-lucide="quote" class="h-16 w-16"></i>
            </div>
            <div class="flex mb-4 space-x-1 relative z-10">
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
            </div>
            <p class="text-slate-700 italic leading-relaxed mb-6 flex-grow relative z-10">
              "Mil-Spec Roofing replaced our roof after storm damage in League City and the whole process was smooth from start to finish. They handled the insurance claim, walked us through every step, and the crew finished the roof replacement in one day. Being veteran-owned, it's clear they run things with real discipline &mdash; showed up on time, cleaned up fully, quality work. Highly recommend for anyone in the Greater Houston area needing a reliable roofing contractor."
            </p>
            <div class="mt-auto border-t border-slate-100 pt-4 relative z-10">
              <h4 class="text-lg font-bold text-slate-900">Amanda Salazar</h4>
              <p class="text-blue-600 text-sm font-semibold uppercase tracking-wide">League City Homeowner</p>
            </div>
          </div>

          <!-- Review 2 -->
          <div class="bg-white p-8 rounded-xl shadow-md border border-slate-100 flex flex-col h-full relative group hover:shadow-lg transition-shadow">
            <div class="absolute top-6 right-6 text-blue-50 transform rotate-180 pointer-events-none group-hover:text-blue-100 transition-colors">
              <i data-lucide="quote" class="h-16 w-16"></i>
            </div>
            <div class="flex mb-4 space-x-1 relative z-10">
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
              <i data-lucide="star" class="h-5 w-5 text-yellow-400 fill-current"></i>
            </div>
            <p class="text-slate-700 italic leading-relaxed mb-6 flex-grow relative z-10">
              "This company is great to deal with. No pressure and honest. I knew I needed a repair or new roof resulting from storm damage, just wasn't sure of the extent. They made recommendations and presented options and didn't hound the insurance company. Ultimately installed a new roof, they did great work and didn't leave a mess."
            </p>
            <div class="mt-auto border-t border-slate-100 pt-4 relative z-10">
              <h4 class="text-lg font-bold text-slate-900">Matthew Carraway</h4>
              <p class="text-blue-600 text-sm font-semibold uppercase tracking-wide">League City Homeowner</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Frequently Asked Questions -->
"@

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$content = $content -replace '(?is)    <!-- Frequently Asked Questions -->', $reviewsSection
[IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
