$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

# =====================================================
# GA4 KEY EVENT TRACKING SCRIPT
# Add to script.js so it loads on every page
# =====================================================
$trackingCode = @"


// =====================================================
// GA4 Key Event Tracking
// =====================================================

document.addEventListener('DOMContentLoaded', function() {

  // --- Phone number click tracking ---
  document.querySelectorAll('a[href^="tel:"]').forEach(function(link) {
    link.addEventListener('click', function() {
      if (typeof gtag === 'function') {
        gtag('event', 'phone_call_click', {
          event_category: 'engagement',
          event_label: link.href,
          value: 1
        });
      }
    });
  });

  // --- Contact form submission tracking ---
  document.querySelectorAll('form').forEach(function(form) {
    form.addEventListener('submit', function() {
      if (typeof gtag === 'function') {
        gtag('event', 'form_submission', {
          event_category: 'conversion',
          event_label: form.action || window.location.pathname,
          value: 1
        });
      }
    });
  });

  // --- CTA button click tracking (Get Free Estimate, Get Free Quote, Request Free Inspection) ---
  document.querySelectorAll('a[href="/contact-us/"], button[type="submit"]').forEach(function(el) {
    var text = (el.textContent || el.innerText || '').trim().toLowerCase();
    if (text.indexOf('estimate') > -1 || text.indexOf('quote') > -1 || text.indexOf('inspection') > -1 || text.indexOf('started') > -1) {
      el.addEventListener('click', function() {
        if (typeof gtag === 'function') {
          gtag('event', 'cta_click', {
            event_category: 'conversion',
            event_label: text,
            value: 1
          });
        }
      });
    }
  });

});
"@

$scriptContent = [IO.File]::ReadAllText("script.js")
if ($scriptContent -notmatch 'GA4 Key Event Tracking') {
    $scriptContent += $trackingCode
    [IO.File]::WriteAllText("script.js", $scriptContent, $utf8NoBom)
    Write-Output "[5] GA4 event tracking appended to script.js"
} else {
    Write-Output "[5] GA4 event tracking already exists in script.js - skipped"
}

# =====================================================
# Wrap phone numbers in clickable tel: links sitewide
# (currently they are plain text, not clickable)
# =====================================================
$files = Get-ChildItem -Path . -Filter "index.html" -Recurse | Where-Object { $_.FullName -notmatch "node_modules" }
$phoneFixed = 0
foreach ($file in $files) {
    $content = [IO.File]::ReadAllText($file.FullName)
    $newContent = $content
    
    # Replace plain-text phone in footer/body (not already wrapped in <a>)
    # Match lines like:  281-813-5925  but NOT already inside an <a> tag
    $newContent = $newContent -replace '(?<!href="[^"]*?)(?<!<a[^>]*?>)(\s*)(281-813-5925)(\s*</)', '$1<a href="tel:+12818135925" class="hover:text-white transition-colors">$2</a>$3'
    
    if ($newContent -ne $content) {
        [IO.File]::WriteAllText($file.FullName, $newContent, $utf8NoBom)
        $phoneFixed++
    }
}
Write-Output "[6] Wrapped phone numbers in tel: links on $phoneFixed pages"
Write-Output "`n=== GA4 tracking complete ==="
