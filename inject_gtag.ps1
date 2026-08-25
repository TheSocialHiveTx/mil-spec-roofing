$gtag = @"

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-P6YMRHQDMT"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-P6YMRHQDMT');
</script>
"@

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$files = Get-ChildItem -Path . -Filter "index.html" -Recurse | Where-Object { $_.FullName -notmatch "node_modules" }
$count = 0

foreach ($file in $files) {
    $content = [IO.File]::ReadAllText($file.FullName)
    
    if ($content -match "G-P6YMRHQDMT") {
        Write-Output "SKIP (already has gtag): $($file.FullName)"
        continue
    }
    
    if ($content -match "<head>") {
        $content = $content -replace "<head>", "<head>$gtag"
        [IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
        $count++
        Write-Output "DONE: $($file.FullName)"
    } elseif ($content -match "<head\s") {
        $content = $content -replace "(<head\s[^>]*>)", "`$1$gtag"
        [IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
        $count++
        Write-Output "DONE: $($file.FullName)"
    } else {
        Write-Output "WARN (no <head> found): $($file.FullName)"
    }
}

Write-Output "`nTotal pages updated: $count"
