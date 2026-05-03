import re
import glob

LOTTIE_CODE = """
<!-- LOTTIE MOVING TRUCK ANIMATION -->
<style>
#lottie-truck-container {
    position: fixed;
    left: -160px;
    top: 50%;
    transform: translateY(-50%);
    width: 140px;
    height: 140px;
    z-index: 99998;
    pointer-events: none;
    animation: truckRide 12s linear infinite;
    opacity: 0.92;
}
@keyframes truckRide {
    0%   { left: -160px; }
    100% { left: calc(100vw + 10px); }
}
@media (max-width: 768px) {
    #lottie-truck-container {
        width: 90px;
        height: 90px;
        animation: truckRide 9s linear infinite;
    }
}
</style>

<script src="https://unpkg.com/@dotlottie/player-component@latest/dist/dotlottie-player.js" type="module"></script>

<div id="lottie-truck-container">
    <dotlottie-player
        src="ottie-ishmjKEnlg.lottie"
        background="transparent"
        speed="1"
        loop
        autoplay
        style="width:100%;height:100%;"
    ></dotlottie-player>
</div>
<!-- END LOTTIE MOVING TRUCK ANIMATION -->
"""

files = glob.glob('**/*.html', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'lottie-truck-container' in content:
        print(f"Skipped (already injected): {file}")
        continue

    # Inject before </body>
    if '</body>' in content:
        new_content = content.replace('</body>', LOTTIE_CODE + '\n</body>', 1)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file}")

print("\nDone. Lottie truck animation injected into all pages.")
