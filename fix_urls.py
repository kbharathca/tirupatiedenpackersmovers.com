import re, glob

files = glob.glob('**/*.html', recursive=True)
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove emoji
    content = re.sub(r'<script id="wp-emoji-settings".*?<\/script>\s*<script type="module">.*?<\/script>\s*', '', content, flags=re.DOTALL)
    
    # Remove speculationrules
    content = re.sub(r'<script type="speculationrules">.*?<\/script>\s*', '', content, flags=re.DOTALL)
    
    # Clean up elementor config URLs
    content = re.sub(r'"urls":\{.*?\}', '"urls":{}', content)
    
    # Clean up elementor lottie default animation url
    content = re.sub(r'"lottie":\{"defaultAnimationUrl":"[^"]*"\}', '"lottie":{"defaultAnimationUrl":""}', content)
    
    # Ensure there are no other wp-content or wp-admin URLs in JSON configs
    content = re.sub(r'"ajaxurl":"[^"]*"', '"ajaxurl":""', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
