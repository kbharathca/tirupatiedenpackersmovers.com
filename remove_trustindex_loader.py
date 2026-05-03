import re, glob

files = glob.glob('**/*.html', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(r'<script[^>]*id="trustindex-loader-js-js"[^>]*>.*?<\/script>\s*', '', content)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Trustindex loader removed.")
