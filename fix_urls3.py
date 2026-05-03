import re, glob

files = glob.glob('**/*.html', recursive=True)
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean up trustindex-google-widget.css
    content = re.sub(r'data-css-url="[^"]*trustindex-google-widget\.css[^"]*"', 'data-css-url=""', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
