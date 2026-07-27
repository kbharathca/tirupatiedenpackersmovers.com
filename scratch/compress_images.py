import os
from PIL import Image

assets_dir = r"e:\Website backups\deccan\tirupatiedenpackersmovers.com\assets"

def compress_image(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png']:
        return False
    try:
        orig_size = os.path.getsize(file_path)
        with Image.open(file_path) as img:
            # Avoid compressing tiny icons or metadata placeholders
            if orig_size < 1024 * 5: # Skip files under 5KB
                return False
            
            # Use original format
            if ext in ['.jpg', '.jpeg']:
                img.save(file_path, "JPEG", optimize=True, quality=75)
            elif ext == '.png':
                # Convert palette to optimize PNG or save with higher compression
                if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                    img.save(file_path, "PNG", optimize=True, compress_level=9)
                else:
                    img.convert("RGB").save(file_path, "JPEG", optimize=True, quality=75)
                    # If we convert png to jpeg, we should keep same filename but format changes.
                    # To keep it extremely simple and not break HTML links, we save PNGs as optimized PNGs.
                    img.save(file_path, "PNG", optimize=True, compress_level=9)
                    
        new_size = os.path.getsize(file_path)
        print(f"Compressed {os.path.basename(file_path)}: {orig_size} -> {new_size} bytes (Saved {orig_size - new_size} bytes)")
        return True
    except Exception as e:
        print(f"Error compressing {file_path}: {e}")
        return False

if __name__ == "__main__":
    count = 0
    for root, _, files in os.walk(assets_dir):
        for f in files:
            full_path = os.path.join(root, f)
            if compress_image(full_path):
                count += 1
    print(f"Done compressing {count} images.")
