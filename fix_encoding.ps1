$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

# roof-repair
$f = "services\roof-repair\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'everywhere in between.*?dedicated', 'everywhere in between&mdash;including dedicated'
[IO.File]::WriteAllText($f, $c, $utf8NoBom)

# roof-replacement
$f = "services\roof-replacement\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'everywhere in between.*?complete', 'everywhere in between&mdash;including complete'
[IO.File]::WriteAllText($f, $c, $utf8NoBom)

# roof-inspection
$f = "services\roof-inspection\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'everywhere in between.*?professional', 'everywhere in between&mdash;including professional'
[IO.File]::WriteAllText($f, $c, $utf8NoBom)

# emergency-roofing
$f = "services\emergency-roofing\index.html"
$c = [IO.File]::ReadAllText($f)
$c = $c -replace 'everywhere in between.*?providing rapid', 'everywhere in between&mdash;providing rapid'
[IO.File]::WriteAllText($f, $c, $utf8NoBom)
