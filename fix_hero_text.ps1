$filePath = "index.html"
$content = Get-Content $filePath -Raw

$oldH1 = '(?is)<h1 class="text-5xl md:text-6xl lg:text-\[4\.5rem\] font-extrabold leading-\[1\.05\] mb-6 drop-shadow-xl uppercase tracking-tight">.*?</h1>'
$newH1 = '<h1 class="text-5xl md:text-6xl lg:text-[4.0rem] font-extrabold leading-[1.05] mb-6 drop-shadow-xl uppercase tracking-tight">
                        Professional Roofing <br class="hidden md:block">
                        <span class="text-blue-400">&amp; Storm Restoration</span> <br class="hidden md:block">
                        Built To Military <br class="hidden md:block">
                        Standards
                    </h1>'

$oldP = '(?is)<p class="text-lg md:text-xl text-slate-300 mb-8 max-w-xl mx-auto lg:mx-0 leading-relaxed">\s*Mil-Spec Roofing delivers dependable roof repair, roof replacement, and storm damage\s*inspections for homeowners and businesses across Southeast Texas\. Our approach emphasizes precision, accountability,\s*and doing the job right the first time\.\s*</p>'
$newP = '<p class="text-lg md:text-xl text-slate-300 mb-8 max-w-xl mx-auto lg:mx-0 leading-relaxed">
                        Mil-Spec Roofing delivers dependable roof repair, roof replacement, and storm damage inspections for homeowners and businesses across Southeast Texas, including comprehensive <a href="/areas-served/league-city/" class="underline text-blue-200 hover:text-white">League City roofing</a> solutions. Our approach emphasizes precision, accountability, and doing the job right the first time.
                    </p>'

if ($content -match $oldH1) { Write-Output "Matched H1" }
if ($content -match $oldP) { Write-Output "Matched P" }

$content = $content -replace $oldH1, $newH1
$content = $content -replace $oldP, $newP

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
Write-Output "Done replacing text."
