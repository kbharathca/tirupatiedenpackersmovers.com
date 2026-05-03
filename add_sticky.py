import re, glob

html_files = glob.glob('**/*.html', recursive=True)

sticky_code = """
<!-- CUSTOM MOBILE STICKY FOOTER -->
<style>
.mobile-sticky-footer {
    display: none;
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 999999;
    box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.08);
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 10px;
    box-sizing: border-box;
    border-top: 1px solid rgba(255,255,255,0.3);
}
.mobile-sticky-footer-inner {
    display: flex;
    gap: 12px;
    justify-content: center;
    align-items: center;
    max-width: 500px;
    margin: 0 auto;
}
.msf-btn {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 14px 0;
    border-radius: 50px;
    color: #fff !important;
    text-decoration: none !important;
    font-weight: 700;
    font-size: 16px;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: transform 0.2s, box-shadow 0.2s;
    font-family: 'Roboto', 'Inter', sans-serif;
    border: 1px solid rgba(255,255,255,0.2);
}
.msf-btn:active {
    transform: scale(0.96);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}
.msf-call {
    background: linear-gradient(135deg, #0052D4, #4364F7, #6FB1FC);
    background-size: 200% 200%;
    animation: gradientShift 5s ease infinite;
}
.msf-whatsapp {
    background: linear-gradient(135deg, #11998e, #38ef7d);
    background-size: 200% 200%;
    animation: gradientShift 5s ease infinite alternate;
}
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.msf-btn i {
    margin-right: 8px;
    font-size: 22px;
}
@media (max-width: 768px) {
    .mobile-sticky-footer {
        display: block;
    }
    body {
        padding-bottom: 80px !important;
    }
}
/* Hide any existing floating buttons on mobile to avoid overlap */
@media (max-width: 768px) {
    .ht-ctc { display: none !important; }
    .joinchat { display: none !important; }
}
</style>
<div class="mobile-sticky-footer">
    <div class="mobile-sticky-footer-inner">
        <a href="tel:+917036153153" class="msf-btn msf-call">
            <i class="fas fa-phone-alt"></i> Call Now
        </a>
        <a href="https://wa.me/917036153153" class="msf-btn msf-whatsapp">
            <i class="fab fa-whatsapp"></i> WhatsApp
        </a>
    </div>
</div>
<!-- END CUSTOM MOBILE STICKY FOOTER -->
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid adding it multiple times
    if "<!-- CUSTOM MOBILE STICKY FOOTER -->" in content:
        continue

    # Insert just before </body>
    if '</body>' in content:
        content = content.replace('</body>', sticky_code + '\n</body>')
    else:
        # If no body tag, just append
        content += sticky_code

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Sticky buttons injected.")
