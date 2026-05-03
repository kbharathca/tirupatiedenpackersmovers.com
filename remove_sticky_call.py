import re, glob

files = glob.glob('**/*.html', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The HTML block
    pattern = r'<div class="quick-call-button"></div>\s*<div class="call-now-button" id="draggable">.*?</div>\s*</a>\s*</div>\s*</div>'
    
    # Remove it
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Also in some places the structure might vary slightly, let's catch just the divs individually if needed
    if new_content == content:
        # Fallback if the strict regex didn't match
        new_content = re.sub(r'<div class="quick-call-button"></div>', '', new_content)
        new_content = re.sub(r'<div class="call-now-button" id="draggable">.*?<div class="quick-alo-phone-img-circle[^>]*></div>\s*</a>\s*</div>\s*</div>', '', new_content, flags=re.DOTALL)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Sticky left call icon removed.")
