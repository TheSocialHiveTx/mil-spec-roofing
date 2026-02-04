import os
import re

root_dir = os.getcwd()
services_dir = os.path.join(root_dir, 'services')

# Regex to find the Google Maps iframe source with the old query
# Old: q=Southeast%20Texas%20Houston
# New: q=Houston%20TX  (Zoomed out z=9 stays the same)

# We'll just target the src string directly
old_query = "q=Southeast%20Texas%20Houston"
new_query = "q=Houston%20TX"

for root, dirs, files in os.walk(services_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_query in content:
                new_content = content.replace(old_query, new_query)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated Map Query in {file_path}")
            else:
                pass
