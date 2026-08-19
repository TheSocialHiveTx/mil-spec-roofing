$f = "services\roof-repair\index.html"
$c = [IO.File]::ReadAllText($f)
if ($c -match "everywhere in between(.*?)dedicated") {
    Write-Output $matches[1]
}
