import re
content = open('index.html', encoding='utf-8').read()

m = re.search(r'<div class="quick-call-button"></div>\s*<div class="call-now-button" id="draggable">.*?</div>\s*</div>\s*</a>\s*</div>\s*</div>', content, re.DOTALL)
if m:
    print(m.group(0))
else:
    # Try a less restrictive match
    m2 = re.search(r'<div class="quick-call-button"></div>.*?<div class="call-now-button"[^>]*>.*?</a>\s*</div>\s*</div>', content, re.DOTALL)
    if m2:
        print(m2.group(0))
    else:
        print("Still not found")
