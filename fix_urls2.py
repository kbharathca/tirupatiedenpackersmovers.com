import re, glob

files = glob.glob('**/*.html', recursive=True)
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We previously replaced URLs with {}
    # We will replace "urls":{} with "urls":{"assets":"data:text/javascript,//"}
    content = re.sub(r'"urls":\{\}', '"urls":{"assets":"data:text/javascript,//"}', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
