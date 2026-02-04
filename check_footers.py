import os

root_dir = "."
missing_footer = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html"):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    if "<footer" not in content:
                        missing_footer.append(filepath)
            except Exception as e:
                print(f"Error reading {filepath}: {e}")

print("Files missing footer:")
for f in missing_footer:
    print(f)
