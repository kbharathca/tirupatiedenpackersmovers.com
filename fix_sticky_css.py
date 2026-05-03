import glob

html_files = glob.glob('**/*.html', recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update the CSS to aggressively hide ht_ctc elements on mobile
    old_css = ".ht-ctc { display: none !important; }"
    new_css = ".ht-ctc { display: none !important; }\n    div[class*=\"ht_ctc\"] { display: none !important; }\n    .ht_ctc_style_2, .ht_ctc_style_7 { display: none !important; }"
    
    if old_css in content:
        content = content.replace(old_css, new_css)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Styles updated.")
