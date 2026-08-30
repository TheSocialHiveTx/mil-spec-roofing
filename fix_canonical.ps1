# =====================================================
# TASK 1: CNAME - Update to www variant
# =====================================================
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText("CNAME", "www.mil-specroofing.com", $utf8NoBom)
Write-Output "[1] CNAME updated to www.mil-specroofing.com"

# =====================================================
# TASK 2: robots.txt - Point sitemap to www
# =====================================================
$robots = @"
User-agent: *
Allow: /
Sitemap: https://www.mil-specroofing.com/sitemap.xml
"@
[IO.File]::WriteAllText("robots.txt", $robots, $utf8NoBom)
Write-Output "[2] robots.txt updated with www sitemap URL"

# =====================================================
# TASK 3: Canonical tags + Schema URLs + all non-www refs -> www
# =====================================================
$files = Get-ChildItem -Path . -Filter "index.html" -Recurse | Where-Object { $_.FullName -notmatch "node_modules" -and $_.FullName -notmatch "test_" }
$count = 0
foreach ($file in $files) {
    $content = [IO.File]::ReadAllText($file.FullName)
    $newContent = $content -replace 'https://mil-specroofing\.com', 'https://www.mil-specroofing.com'
    if ($newContent -ne $content) {
        [IO.File]::WriteAllText($file.FullName, $newContent, $utf8NoBom)
        $count++
    }
}
Write-Output "[3] Updated $count HTML files: all https://mil-specroofing.com -> https://www.mil-specroofing.com"

# =====================================================
# TASK 4: Sitemap - Regenerate with www URLs
# =====================================================
$sitemapContent = [IO.File]::ReadAllText("sitemap.xml")
$sitemapContent = $sitemapContent -replace 'https://mil-specroofing\.com', 'https://www.mil-specroofing.com'
[IO.File]::WriteAllText("sitemap.xml", $sitemapContent, $utf8NoBom)
Write-Output "[4] sitemap.xml updated with www URLs"

Write-Output "`n=== Infrastructure fixes complete ==="
