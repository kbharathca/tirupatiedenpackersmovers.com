import re
content = open('index.html', encoding='utf-8').read()
matches = re.finditer(r'<div[^>]*class="[^"]*call[^"]*"[^>]*>', content, re.IGNORECASE)
for m in matches:
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 300)
    print("MATCH:", content[start:end])
    print("---------------------------------")
