import re
import glob

# SEO keyword pool for Tirupati Packers and Movers
alt_pool = [
    "Packers and Movers in Tirupati",
    "Best Packers and Movers Tirupati",
    "House Shifting in Tirupati",
    "Home Relocation Services Tirupati",
    "Household Goods Shifting Tirupati",
    "Office Shifting Tirupati",
    "Bike Transport Tirupati",
    "Car Transport Tirupati",
    "Loading Unloading Services Tirupati",
    "Professional Movers Tirupati",
    "Safe Packing Services Tirupati",
    "Furniture Shifting Tirupati Andhra Pradesh",
    "Eden Packers and Movers Tirupati",
    "Affordable Packers Movers Tirupati",
    "Local Shifting Services Tirupati",
    "Intercity Relocation Tirupati",
    "Luggage Transport Tirupati",
    "Household Shifting Experts Tirupati",
    "Reliable Movers and Packers Tirupati",
    "Moving Company Tirupati Andhra Pradesh",
]

files = glob.glob('**/*.html', recursive=True)

counter = 0

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_img(m):
        global counter
        tag = m.group(0)
        
        # Skip if already has a meaningful alt (not empty)
        existing_alt = re.search(r'alt="([^"]*)"', tag, re.IGNORECASE)
        if existing_alt and existing_alt.group(1).strip():
            # Already has alt text - skip
            return tag
        
        # Pick from pool cyclically
        alt_text = alt_pool[counter % len(alt_pool)]
        counter += 1
        
        if existing_alt:
            # Replace empty alt with keyword alt
            tag = re.sub(r'alt=""', f'alt="{alt_text}"', tag)
            tag = re.sub(r"alt=''", f"alt='{alt_text}'", tag)
        else:
            # Insert alt attribute before closing > or />
            tag = re.sub(r'(\s*/?>)$', f' alt="{alt_text}"\\1', tag.rstrip())
        
        return tag

    new_content = re.sub(r'<img\b[^>]*>', replace_img, content, flags=re.IGNORECASE | re.DOTALL)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file}")

print(f"\nDone. Added/updated alt text on {counter} images across all HTML files.")
