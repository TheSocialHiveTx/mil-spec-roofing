import os
import re

def remove_about_links(file_path):
    """Remove all about-us links from an HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern 1: Desktop nav link (with the "About" text)
        # <a href="/about-us/" class="nav-link text-sm font-bold uppercase tracking-wide text-slate-600 hover:text-blue-500">About</a>
        content = re.sub(
            r'\s*<a href="/about-us/" class="nav-link[^"]*"[^>]*>About</a>\s*',
            '\n',
            content
        )
        
        # Pattern 2: Mobile nav link (with the "About" text)
        # <a href="/about-us/" class="mobile-nav-link text-sm font-bold uppercase text-slate-600 py-2 block">About</a>
        content = re.sub(
            r'\s*<a href="/about-us/" class="mobile-nav-link[^"]*"[^>]*>About</a>\s*',
            '\n',
            content
        )
        
        # Pattern 3: Footer link (with the "About Us" text within <li>)
        # <li><a href="/about-us/" class="hover:text-white transition-colors">About Us</a></li>
        content = re.sub(
            r'\s*<li>\s*<a href="/about-us/"[^>]*>About Us</a>\s*</li>\s*',
            '\n',
            content
        )
        
        # Pattern 4: Multi-line desktop nav link (used in some city pages)
        # Remove the entire multi-line anchor block
        content = re.sub(
            r'\s*<a href="/about-us/"\s+class="nav-link[^"]*"[^>]*>\s*About\s*</a>\s*',
            '\n',
            content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# Find all HTML files
html_files = []
for root, dirs, files in os.walk('.'):
    # Skip images and other non-relevant directories
    if 'images' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

print(f"Found {len(html_files)} HTML files")

updated_count = 0
for file_path in html_files:
    if remove_about_links(file_path):
        updated_count += 1
        print(f"Updated: {file_path}")

print(f"\n✓ Updated {updated_count}/{len(html_files)} files")
