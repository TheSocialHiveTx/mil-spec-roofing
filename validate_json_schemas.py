import os
import json
import re

def validate_json_ld(file_path):
    """Validate JSON-LD schema in HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'application/ld+json' not in content:
            return True, "No schema"
        
        # Extract JSON-LD
        pattern = r'<script type="application/ld\+json">(.*?)</script>'
        matches = re.findall(pattern, content, re.DOTALL)
        
        if not matches:
            return False, "Schema tag found but no content"
        
        errors = []
        for i, match in enumerate(matches):
            try:
                # Try to parse JSON
                schema_text = match.strip()
                schema = json.loads(schema_text)
                
                # Check for duplicate keys by parsing as text
                # Count occurrences of keys
                if '"sameAs"' in schema_text:
                    sameas_count = schema_text.count('"sameAs":')
                    if sameas_count > 2:  # Allow 2 (one in org, one in localbusiness)
                        # Check if they're in same object
                        lines = schema_text.split('\n')
                        same_as_lines = [i for i, line in enumerate(lines) if '"sameAs":' in line]
                        if len(same_as_lines) >= 2:
                            # Check if distance is too close (within same object)
                            for j in range(len(same_as_lines) - 1):
                                if same_as_lines[j+1] - same_as_lines[j] < 15:  # Too close, likely duplicate
                                    errors.append(f"Schema {i+1}: Duplicate 'sameAs' key detected")
                
            except json.JSONDecodeError as e:
                errors.append(f"Schema {i+1}: JSON parsing error - {str(e)}")
            except Exception as e:
                errors.append(f"Schema {i+1}: Error - {str(e)}")
        
        if errors:
            return False, "; ".join(errors)
        return True, "Valid"
        
    except Exception as e:
        return False, f"File error: {str(e)}"

# Check all HTML files
print("=" * 80)
print("JSON-LD SCHEMA VALIDATION")
print("=" * 80)

files_to_check = []
for root, dirs, files in os.walk('.'):
    if 'images' in root or 'node_modules' in root:
        continue
    for file in files:
        if file == 'index.html':
            files_to_check.append(os.path.join(root, file))

invalid_files = []
for file_path in sorted(files_to_check):
    is_valid, message = validate_json_ld(file_path)
    if not is_valid:
        invalid_files.append((file_path, message))
        print(f"\n❌ {file_path}")
        print(f"   {message}")

print(f"\n{'=' * 80}")
if invalid_files:
    print(f"⚠ Found {len(invalid_files)} files with JSON errors")
else:
    print(f"✅ All {len(files_to_check)} files have valid JSON-LD schemas")
print("=" * 80)
