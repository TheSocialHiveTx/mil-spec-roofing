# index.html
$f = "index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'across Southeast Texas\. Our approach emphasizes', 'across Southeast Texas, including comprehensive <a href="/areas-served/league-city/" class="underline text-blue-200 hover:text-white">League City roofing</a> solutions. Our approach emphasizes'
[IO.File]::WriteAllText($f, $c)

# roof-repair
$f = "services\roof-repair\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'From Houston to Galveston, and everywhere in between\. Our teams are deployed across the region\.', 'From Houston to Galveston, and everywhere in between—including dedicated <a href="/areas-served/league-city/" class="text-blue-600 hover:underline">roof repair in League City</a>. Our teams are deployed across the region.'
[IO.File]::WriteAllText($f, $c)

# roof-replacement
$f = "services\roof-replacement\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'From Houston to Galveston, and everywhere in between\. Our teams are deployed across the region\.', 'From Houston to Galveston, and everywhere in between—including complete <a href="/areas-served/league-city/" class="text-blue-600 hover:underline">League City roof replacements</a>. Our teams are deployed across the region.'
[IO.File]::WriteAllText($f, $c)

# roof-inspection
$f = "services\roof-inspection\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'From Houston to Galveston, and everywhere in between\. Our teams are deployed across the region\.', 'From Houston to Galveston, and everywhere in between—including professional <a href="/areas-served/league-city/" class="text-blue-600 hover:underline">League City roof inspections</a>. Our teams are deployed across the region.'
[IO.File]::WriteAllText($f, $c)

# emergency-roofing
$f = "services\emergency-roofing\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'From Houston to Galveston, and everywhere in between\. Our teams are deployed across the region\.', 'From Houston to Galveston, and everywhere in between—providing rapid <a href="/areas-served/league-city/" class="text-blue-600 hover:underline">emergency roofing in League City</a> and beyond. Our teams are deployed across the region.'
[IO.File]::WriteAllText($f, $c)

# residential-roofing
$f = "services\residential-roofing\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'From Houston to Galveston, and everywhere in between\. Our teams are deployed across the region\.', 'From Houston to Galveston, and everywhere in between. If you need trusted <a href="/areas-served/league-city/" class="text-blue-600 hover:underline">residential roofing in League City</a> or surrounding areas, our teams are deployed across the region.'
[IO.File]::WriteAllText($f, $c)

# commercial-roofing
$f = "services\commercial-roofing\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'From Houston to Galveston, and everywhere in between\. Our teams are deployed across the region\.', 'From Houston to Galveston, and everywhere in between. For businesses seeking reliable <a href="/areas-served/league-city/" class="text-blue-600 hover:underline">commercial roofing in League City</a>, our teams are deployed across the region.'
[IO.File]::WriteAllText($f, $c)

# project-gallery
$f = "project-gallery\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'Explore our recent residential and commercial operations\.', 'Explore our recent residential and commercial operations, including top-tier projects from your trusted <a href="/areas-served/league-city/" class="text-blue-600 hover:underline">League City roofing contractor</a>.'
[IO.File]::WriteAllText($f, $c)
