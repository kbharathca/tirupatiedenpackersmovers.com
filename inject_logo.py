import re
import glob

LOGO_PATH = "assets/eden-logo.png"
LOGO_ALT = "Eden Packers and Movers Tirupati Logo"

# 1. FAVICON TAGS to inject into <head> (right after <head> tag)
FAVICON_TAGS = f"""
<!-- EDEN PACKERS & MOVERS FAVICON -->
<link rel="icon" type="image/png" sizes="512x512" href="{LOGO_PATH}">
<link rel="apple-touch-icon" sizes="512x512" href="{LOGO_PATH}">
<link rel="shortcut icon" href="{LOGO_PATH}">
<!-- END FAVICON -->
"""

# 2. FOOTER LOGO HTML to inject before </footer>
FOOTER_LOGO = f"""
<!-- FOOTER LOGO BRAND -->
<div style="
    text-align: center;
    padding: 30px 20px 20px;
    background: linear-gradient(135deg, #0a1628 0%, #1a2d50 100%);
    border-top: 3px solid #f39c12;
">
    <img src="{LOGO_PATH}"
         alt="{LOGO_ALT}"
         style="width: 90px; height: 90px; border-radius: 16px; box-shadow: 0 8px 25px rgba(243,156,18,0.35); object-fit: cover; margin-bottom: 14px; display: block; margin-left: auto; margin-right: auto;">
    <div style="color: #fff; font-size: 20px; font-weight: 800; letter-spacing: 1px; font-family: 'Inter', 'Roboto', sans-serif; margin-bottom: 4px;">
        EDEN PACKERS &amp; MOVERS
    </div>
    <div style="color: #f39c12; font-size: 13px; font-weight: 500; letter-spacing: 2px; text-transform: uppercase; font-family: 'Inter', 'Roboto', sans-serif; margin-bottom: 12px;">
        Tirupati, Andhra Pradesh
    </div>
    <div style="color: rgba(255,255,255,0.55); font-size: 13px; font-family: 'Inter', 'Roboto', sans-serif;">
        &copy; 2026 Eden Packers &amp; Movers. All rights reserved.
    </div>
</div>
<!-- END FOOTER LOGO BRAND -->
"""

files = glob.glob('**/*.html', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # --- Inject Favicon into <head> ---
    if "EDEN PACKERS & MOVERS FAVICON" not in new_content:
        new_content = re.sub(
            r'(<head[^>]*>)',
            r'\1\n' + FAVICON_TAGS,
            new_content,
            count=1,
            flags=re.IGNORECASE
        )
    
    # --- Inject Footer Logo before </footer> ---
    if "FOOTER LOGO BRAND" not in new_content:
        new_content = new_content.replace('</footer>', FOOTER_LOGO + '\n</footer>', 1)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file}")

print("\nDone. Favicon and footer logo injected across all pages.")
