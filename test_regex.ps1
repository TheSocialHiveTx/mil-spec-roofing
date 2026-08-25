$filePath = "services\roof-repair\index.html"
$content = Get-Content $filePath -Raw

$pattern1 = '(?is)(<div class="bg-white shadow-xl rounded-lg border border-slate-100 overflow-hidden flex\s*flex-col max-h-\[80vh\] overflow-y-auto">)\s*<a href="[^"]+" class="block px-4 py-3 text-sm text-slate-600\s*hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">[^<]+</a>'
$replacement1 = '$1
                              <a href="/services/residential-roofing/" class="block px-4 py-3 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 border-b border-slate-50 transition-colors">Residential Roofing</a>'

$pattern2 = '(?is)(<h4 class="font-bold text-slate-900 uppercase tracking-wider mb-4">Our Services</h4>\s*<ul class="space-y-3">)\s*<li><a href="[^"]+" class="block py-2 text-slate-600 hover:text-blue-600\s*hover:pl-2 transition-all border-b border-slate-100">[^<]+</a></li>'
$replacement2 = '$1
                            <li><a href="/services/residential-roofing/" class="block py-2 text-slate-600 hover:text-blue-600 hover:pl-2 transition-all border-b border-slate-100">Residential Roofing</a></li>'

$pattern3 = '(?is)(<h4 class="text-white font-bold uppercase tracking-wider mb-6">Services</h4>\s*<ul class="space-y-3 text-sm">)\s*<li><a href="[^"]+"\s*class="hover:text-white transition-colors">Residential\s*Roofing</a></li>'
$replacement3 = '$1
                        <li><a href="/services/residential-roofing/" class="hover:text-white transition-colors">Residential Roofing</a></li>'

if ($content -match $pattern1) { Write-Output "Nav matched" }
if ($content -match $pattern2) { Write-Output "Sidebar matched" }
if ($content -match $pattern3) { Write-Output "Footer matched" }

$content = $content -replace $pattern1, $replacement1
$content = $content -replace $pattern2, $replacement2
$content = $content -replace $pattern3, $replacement3

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText("test_roof_repair.html", $content, $utf8NoBom)
