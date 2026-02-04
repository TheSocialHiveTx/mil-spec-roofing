import os
import re

def optimize_html_file(file_path):
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Optimize Images
    # Find all img tags
    # We use a function replacement to check attributes
    def replace_img(match):
        full_tag = match.group(0)
        
        # Skip if already has loading attribute
        if 'loading=' in full_tag:
            return full_tag
            
        # Insert loading="lazy" before the closing tag
        # Use simple replacement of the end of the tag
        if '/>' in full_tag:
            return full_tag.replace('/>', ' loading="lazy" />')
        else:
            return full_tag.replace('>', ' loading="lazy">')

    # Regex for img tag: <img [stuff] >
    # Non-greedy match until >
    content = re.sub(r'<img\s[^>]*?>', replace_img, content, flags=re.IGNORECASE)

    # 2. Optimize Iframes
    def replace_iframe(match):
        full_tag = match.group(0)
        
        # Skip if already has loading attribute
        if 'loading=' in full_tag:
            return full_tag
            
        # Insert loading="lazy"
        # Often iframes are <iframe src="..."></iframe>
        # We target the opening tag
        if '/>' in full_tag:
             return full_tag.replace('/>', ' loading="lazy" />')
        else:
             return full_tag.replace('>', ' loading="lazy">')

    # Regex for iframe OPENING tag: <iframe [stuff] >
    content = re.sub(r'<iframe\s[^>]*?>', replace_iframe, content, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Main Execution
root_dir = "."
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html"):
            if "node_modules" in dirpath or ".git" in dirpath:
                continue
                
            file_path = os.path.join(dirpath, filename)
            try:
                optimize_html_file(file_path)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print("Lazy loading applied to all images and iframes.")
