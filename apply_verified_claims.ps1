$filePath = "areas-served\galveston\index.html"
$content = [IO.File]::ReadAllText($filePath)

# 1. Update the "Roof Replacement" card paragraph
$oldRoofReplacement = 'When salt air and time have compromised your decking, we execute complete <a href="/services/roof-replacement/" class="text-blue-600 font-semibold hover:underline">roof replacements</a>. We install windstorm-certified, marine-grade systems built explicitly for the island''s extreme demands.'
$newRoofReplacement = 'When salt air and time have compromised your decking, we execute complete <a href="/services/roof-replacement/" class="text-blue-600 font-semibold hover:underline">roof replacements</a>. We install CertainTeed roofing systems that meet TDI Windstorm Inspection Program requirements, using corrosion-resistant fasteners built explicitly for the island''s extreme demands.'
$content = $content -replace [regex]::Escape($oldRoofReplacement), $newRoofReplacement

# 2. Replace the old "salt air" FAQ with the new fasteners FAQ
$oldSaltAirFaq = @"
            <div class="bg-slate-50 border border-slate-100 rounded-lg p-6">
              <h3 class="text-lg font-bold text-slate-900 mb-2">How does salt air affect Galveston roofs?</h3>
              <p class="text-slate-600">
                Salt air corrodes standard materials quickly. We use marine-grade fasteners and corrosion-resistant components to ensure long-term durability in coastal conditions.
              </p>
            </div>
"@
$newFastenersFaq = @"
            <div class="bg-slate-50 border border-slate-100 rounded-lg p-6">
              <h3 class="text-lg font-bold text-slate-900 mb-2">What fasteners are used for roofing projects in Galveston?</h3>
              <p class="text-slate-600 mb-4">
                For coastal roofing projects in Galveston, Mil-Spec Roofing &amp; Construction follows applicable roofing requirements for high-wind coastal construction. Asphalt shingle installations use corrosion-resistant galvanized steel or stainless-steel roofing nails where required, with fastener specifications appropriate for the roofing system and manufacturer installation requirements.
              </p>
              <p class="text-slate-600">
                Texas Department of Insurance (TDI) guidance specifies galvanized steel or stainless-steel roofing nails with a minimum 12-gauge (0.105-inch) shank and a minimum 3/8-inch head for applicable asphalt shingle installations. Staples are not permitted.
              </p>
            </div>
"@
# Normalize line endings to avoid regex failures
$content = $content -replace '(?is)<div class="bg-slate-50 border border-slate-100 rounded-lg p-6">\s*<h3 class="text-lg font-bold text-slate-900 mb-2">How does salt air affect Galveston roofs\?</h3>.*?</div>', $newFastenersFaq

# 3. Replace the old "hurricanes" FAQ with the new windstorm standards FAQ
$oldHurricaneFaq = @"
            <div class="bg-slate-50 border border-slate-100 rounded-lg p-6">
              <h3 class="text-lg font-bold text-slate-900 mb-2">What materials work best in Galveston hurricanes?</h3>
              <p class="text-slate-600">
                Impact-resistant materials and enhanced fastening systems help manage hurricane winds. We also focus on construction that meets coastal building codes.
              </p>
            </div>
"@
$newWindstormFaq = @"
            <div class="bg-slate-50 border border-slate-100 rounded-lg p-6">
              <h3 class="text-lg font-bold text-slate-900 mb-2">What windstorm standards apply to roof replacements in Galveston?</h3>
              <p class="text-slate-600 mb-4">
                Roofing projects in Galveston are completed with consideration for applicable Texas Department of Insurance (TDI) Windstorm Inspection Program requirements, manufacturer installation specifications, and coastal wind-resistance requirements.
              </p>
              <p class="text-slate-600 mb-4">
                For Windstorm Certificate of Compliance applications beginning April 1, 2026, TDI uses the 2024 International Residential Code (IRC) or 2024 International Building Code (IBC), as applicable. Required design wind speeds are determined based on the specific location and characteristics of the structure.
              </p>
              <p class="text-slate-600 mb-4">
                For asphalt roofing systems, TDI requires qualifying shingles to indicate compliance with ASTM D3161 or ASTM D7158 wind-resistance testing standards. TDI recommends shingles tested to ASTM D3161 Class F or ASTM D7158 Class H for high-wind applications.
              </p>
              <p class="text-slate-600">
                Mil-Spec uses CertainTeed roofing products and installs roofing systems according to applicable manufacturer specifications and project-specific coastal construction requirements.
              </p>
            </div>
"@
$content = $content -replace '(?is)<div class="bg-slate-50 border border-slate-100 rounded-lg p-6">\s*<h3 class="text-lg font-bold text-slate-900 mb-2">What materials work best in Galveston hurricanes\?</h3>.*?</div>', $newWindstormFaq


$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
