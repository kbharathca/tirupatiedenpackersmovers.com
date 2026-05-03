import re, glob

files = glob.glob('**/*.html', recursive=True)
total_imgs = 0
with_alt = 0
empty_alt = 0
no_alt = 0

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    imgs = re.findall(r'<img\b[^>]*>', content, re.IGNORECASE | re.DOTALL)
    for img in imgs:
        total_imgs += 1
        alt_match = re.search(r'alt="([^"]*)"', img, re.IGNORECASE)
        if not alt_match:
            no_alt += 1
            print(f"NO ALT in {file}: {img[:120]}")
        elif not alt_match.group(1).strip():
            empty_alt += 1
            print(f"EMPTY ALT in {file}: {img[:120]}")
        else:
            with_alt += 1

print(f"\n--- SUMMARY ---")
print(f"Total images: {total_imgs}")
print(f"With keyword alt: {with_alt}")
print(f"Empty alt: {empty_alt}")
print(f"Missing alt entirely: {no_alt}")
