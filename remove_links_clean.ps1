$pattern = '(?s)\s*<a href="/services/metal-roofing/"[^>]*>.*?Metal\s*Roofing</a>'
Get-ChildItem -Path . -Recurse -Include *.html,*.py -Exclude node_modules,.git | ForEach-Object {
    $content = [IO.File]::ReadAllText($_.FullName)
    if ($content -match $pattern) {
        $newContent = $content -replace $pattern, ''
        [IO.File]::WriteAllText($_.FullName, $newContent)
        Write-Output "Updated $($_.FullName)"
    }
}
