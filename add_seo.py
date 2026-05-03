import glob, re

seo_script = """
<!-- LOCAL BUSINESS SEO SCHEMA FOR GOOGLE MAPS -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MovingCompany",
  "name": "Eden Packers & Movers",
  "@id": "https://www.google.com/maps/place/Eden+Packers+%26+Movers/@13.6395534,79.4257339,17z/data=!3m1!4b1!4m6!3m5!1s0x3a4d4b24b26937cd:0x33fd73de6fdc8844!8m2!3d13.6395534!4d79.4283088!16s%2Fg%2F11k7b7yfm9",
  "url": "https://tirupatiedenpackersmovers.com",
  "telephone": "+917036153153",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Tirupati",
    "addressRegion": "Andhra Pradesh",
    "addressCountry": "IN"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 13.6395534,
    "longitude": 79.4283088
  },
  "hasMap": "https://www.google.com/maps/place/Eden+Packers+%26+Movers/@13.6395534,79.4257339,17z/data=!3m1!4b1!4m6!3m5!1s0x3a4d4b24b26937cd:0x33fd73de6fdc8844!8m2!3d13.6395534!4d79.4283088!16s%2Fg%2F11k7b7yfm9",
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "opens": "00:00",
    "closes": "23:59"
  }
}
</script>
<!-- END LOCAL BUSINESS SEO SCHEMA -->
"""

seo_link = """
<div class="google-maps-seo-link" style="text-align:center; padding: 15px; font-weight: bold; background: #fdfbfb; border: 1px solid #eee; border-radius: 8px; margin-top: 10px;">
    <a href="https://www.google.com/maps/place/Eden+Packers+%26+Movers/@13.6395534,79.4257339,17z/data=!3m1!4b1!4m6!3m5!1s0x3a4d4b24b26937cd:0x33fd73de6fdc8844!8m2!3d13.6395534!4d79.4283088!16s%2Fg%2F11k7b7yfm9" target="_blank" rel="noopener noreferrer" style="color:#0072ff; text-decoration:none; display: flex; align-items: center; justify-content: center; gap: 8px;">
        <i class="fas fa-map-marker-alt" style="color:#ea4335; font-size:18px;"></i> View Eden Packers & Movers on Google Maps (Verified Listing)
    </a>
</div>
"""

files = glob.glob('**/*.html', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # 1. Inject JSON-LD Schema into <head>
    if "LOCAL BUSINESS SEO SCHEMA FOR GOOGLE MAPS" not in new_content:
        new_content = re.sub(r'(<head[^>]*>)', r'\1\n' + seo_script, new_content, count=1, flags=re.IGNORECASE)
    
    # 2. Add explicit SEO link below maps iframes
    if "<iframe" in new_content and "maps.google.com" in new_content:
        if "google-maps-seo-link" not in new_content:
            # We insert it right after the closing </iframe> for any maps iframe
            new_content = re.sub(r'(<iframe[^>]*maps\.google\.com[^>]*><\/iframe>)', r'\1\n' + seo_link, new_content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("SEO tags and Maps link updated.")
