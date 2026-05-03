import re
content = open('index.html', encoding='utf-8').read()

print("--- Sticky matching ---")
matches = re.findall(r'<[^>]*class="[^"]*sticky[^"]*"[^>]*>', content, re.IGNORECASE)
for m in set(matches):
    print(m)

print("--- Float matching ---")
matches = re.findall(r'<[^>]*class="[^"]*float[^"]*"[^>]*>', content, re.IGNORECASE)
for m in set(matches):
    print(m)

print("--- Call matching ---")
matches = re.findall(r'<[^>]*class="[^"]*call[^"]*"[^>]*>', content, re.IGNORECASE)
for m in set(matches[:10]):
    print(m)
