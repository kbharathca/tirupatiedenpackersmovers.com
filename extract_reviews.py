import json
from bs4 import BeautifulSoup

content = open('index.html', encoding='utf-8').read()
soup = BeautifulSoup(content, 'html.parser')

template = soup.find('template', id='trustindex-google-widget-html')
if not template:
    print("Template not found.")
    exit()

template_content = template.string or ''.join(str(c) for c in template.contents)
template_soup = BeautifulSoup(template_content, 'html.parser')

reviews = template_soup.find_all('div', class_='ti-review-item')

extracted = []
for r in reviews:
    name_el = r.find('div', class_='ti-name')
    date_el = r.find('div', class_='ti-date')
    text_el = r.find('div', class_='ti-review-text-container')
    
    profile_img_el = r.select_one('.ti-profile-img trustindex-image')
    
    if name_el and text_el:
        name = name_el.get_text(strip=True)
        # text container has <!-- R-CONTENT --> comments, get_text might work
        text = text_el.get_text(strip=True)
        date = date_el.get_text(strip=True) if date_el else ''
        img = profile_img_el.get('data-imgurl', '') if profile_img_el else ''
        
        # Only keep reviews with text
        if text:
            extracted.append({'name': name, 'text': text, 'date': date, 'img': img})

with open('reviews.json', 'w', encoding='utf-8') as f:
    json.dump(extracted, f, indent=4)

print(f"Extracted {len(extracted)} reviews.")
