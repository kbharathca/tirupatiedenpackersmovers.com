import os
from PIL import Image

assets_dir = r"e:\Website backups\deccan\tirupatiedenpackersmovers.com\assets"
limit_bytes = 150 * 1024

def compress_to_limit(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png']:
        return False
    
    orig_size = os.path.getsize(file_path)
    if orig_size <= limit_bytes:
        return False

    try:
        # Don't destroy transparency or aspect ratio. 
        # For PNG, if size exceeds 150KB, we can reduce its resolution, quality, or colors.
        with Image.open(file_path) as img:
            quality = 70
            width, height = img.size
            
            # Step 1: Try lowering saving quality for JPG
            if ext in ['.jpg', '.jpeg']:
                img.save(file_path, "JPEG", optimize=True, quality=quality)
                if os.path.getsize(file_path) <= limit_bytes:
                    print(f"Compressed {os.path.basename(file_path)} under 150KB via quality reduction.")
                    return True
            
            # Step 2: If still > 150KB, or if it is a PNG, downscale resolution progressively
            for scale in [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]:
                new_size = (int(width * scale), int(height * scale))
                resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                
                if ext in ['.jpg', '.jpeg']:
                    resized_img.save(file_path, "JPEG", optimize=True, quality=65)
                elif ext == '.png':
                    resized_img.save(file_path, "PNG", optimize=True, compress_level=9)
                
                if os.path.getsize(file_path) <= limit_bytes:
                    print(f"Compressed {os.path.basename(file_path)} under 150KB by resizing to {new_size}.")
                    return True
            
            # Step 3: Extreme fallback if still over limit (e.g. convert PNG to JPG if name extension doesn't match, or force lower quality)
            if ext in ['.jpg', '.jpeg']:
                img.resize((int(width * 0.25), int(height * 0.25)), Image.Resampling.LANCZOS).save(file_path, "JPEG", optimize=True, quality=50)
            elif ext == '.png':
                # Force quantize to 256 colors palette mode to compress PNG heavily
                quantized = img.quantize(colors=256)
                quantized.save(file_path, "PNG", optimize=True)
                if os.path.getsize(file_path) <= limit_bytes:
                    print(f"Compressed {os.path.basename(file_path)} under 150KB by quantizing colors.")
                    return True
                
                # Resize + Quantize
                resized_quantized = img.resize((int(width * 0.5), int(height * 0.5)), Image.Resampling.LANCZOS).quantize(colors=256)
                resized_quantized.save(file_path, "PNG", optimize=True)
                print(f"Force compressed PNG {os.path.basename(file_path)} under 150KB via scale & quantization.")
                return True
                
        return True
    except Exception as e:
        print(f"Error compressing {file_path}: {e}")
        return False

if __name__ == "__main__":
    count = 0
    for root, _, files in os.walk(assets_dir):
        for f in files:
            full_path = os.path.join(root, f)
            if compress_to_limit(full_path):
                count += 1
    print(f"Forced {count} images to be under 150KB.")
