$results = @()
Get-ChildItem -Path . -Recurse -Filter *.html | Where-Object { $_.FullName -notmatch '\\node_modules\\' -and $_.FullName -notmatch '\\.git\\' } | ForEach-Object {
    $content = [IO.File]::ReadAllText($_.FullName)
    $canonical = ""
    $noindex = $false
    
    if ($content -match '<link\s+rel="canonical"\s+href="([^"]+)"') {
        $canonical = $matches[1]
    } elseif ($content -match '<link\s+href="([^"]+)"\s+rel="canonical"') {
        $canonical = $matches[1]
    }
    
    if ($content -match 'noindex') {
        $noindex = $true
    }
    
    $results += [PSCustomObject]@{
        File = $_.FullName.Replace($PWD.Path + '\', '')
        Canonical = $canonical
        NoIndex = $noindex
    }
}
$results | Export-Csv -Path "canonicals_report.csv" -NoTypeInformation
