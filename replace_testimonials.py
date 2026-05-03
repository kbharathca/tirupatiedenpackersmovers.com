import re

new_html = """
<!-- CUSTOM STUNNING TESTIMONIALS SLIDER -->
<link rel="stylesheet" href="https://unpkg.com/swiper@8/swiper-bundle.min.css" />
<style>
.custom-testimonials-section {
    padding: 80px 20px;
    background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    overflow: hidden;
    position: relative;
}
.custom-testimonials-section::before {
    content: '';
    position: absolute;
    top: -100px;
    right: -100px;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(0,198,255,0.15) 0%, rgba(0,114,255,0) 70%);
    border-radius: 50%;
    z-index: 1;
}
.custom-testimonials-section::after {
    content: '';
    position: absolute;
    bottom: -100px;
    left: -100px;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(37,211,102,0.15) 0%, rgba(18,140,126,0) 70%);
    border-radius: 50%;
    z-index: 1;
}
.testi-header {
    text-align: center;
    margin-bottom: 50px;
    position: relative;
    z-index: 2;
}
.testi-header h2 {
    font-size: 36px;
    font-weight: 800;
    color: #2d3436;
    margin-bottom: 15px;
    font-family: 'Inter', sans-serif;
}
.testi-header p {
    font-size: 16px;
    color: #636e72;
    max-width: 600px;
    margin: 0 auto;
}
.swiper-testimonials {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding-bottom: 60px;
    z-index: 2;
}
.testi-card {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
}
.testi-card::before {
    content: '\\f10d';
    font-family: 'Font Awesome 5 Free';
    font-weight: 900;
    position: absolute;
    top: 20px;
    right: 20px;
    font-size: 40px;
    color: rgba(0, 114, 255, 0.05);
    z-index: 0;
}
.testi-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 114, 255, 0.1);
}
.testi-stars {
    color: #fdcb6e;
    font-size: 14px;
    margin-bottom: 15px;
    position: relative;
    z-index: 1;
}
.testi-text {
    font-size: 16px;
    line-height: 1.6;
    color: #2d3436;
    margin-bottom: 25px;
    font-style: italic;
    position: relative;
    z-index: 1;
}
.testi-author {
    display: flex;
    align-items: center;
    position: relative;
    z-index: 1;
}
.testi-avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 15px;
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-weight: bold;
    font-size: 20px;
}
.testi-avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}
.testi-info h4 {
    margin: 0;
    font-size: 16px;
    color: #2d3436;
    font-weight: 700;
}
.testi-info span {
    font-size: 13px;
    color: #636e72;
}
.swiper-pagination-bullet {
    background: #0072ff;
    opacity: 0.5;
}
.swiper-pagination-bullet-active {
    opacity: 1;
    transform: scale(1.2);
}
</style>

<section class="custom-testimonials-section">
    <div class="testi-header">
        <h2>What Our Clients Say</h2>
        <p>Trusted by hundreds of families and businesses. Here is what they have to say about our moving services.</p>
    </div>

    <div class="swiper swiper-testimonials">
        <div class="swiper-wrapper">
            <!-- Testimonial 1 -->
            <div class="swiper-slide">
                <div class="testi-card">
                    <div>
                        <div class="testi-stars">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="testi-text">"Nice service by Eden Packers & Movers. The staff was highly professional and packing was done with utmost care. Highly recommended!"</p>
                    </div>
                    <div class="testi-author">
                        <div class="testi-avatar">RR</div>
                        <div class="testi-info">
                            <h4>Revanth Revanth</h4>
                            <span>Verified Customer</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Testimonial 2 -->
            <div class="swiper-slide">
                <div class="testi-card">
                    <div>
                        <div class="testi-stars">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="testi-text">"I had a wonderful experience shifting my household goods. Very prompt, communicative, and delivered everything on time without any damage."</p>
                    </div>
                    <div class="testi-author">
                        <div class="testi-avatar">RB</div>
                        <div class="testi-info">
                            <h4>Ravindra Reddy Basireddy</h4>
                            <span>Verified Customer</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Testimonial 3 -->
            <div class="swiper-slide">
                <div class="testi-card">
                    <div>
                        <div class="testi-stars">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="testi-text">"Excellent service from start to finish. Their team handled all my fragile items perfectly. Hands down the best packers in the city."</p>
                    </div>
                    <div class="testi-author">
                        <div class="testi-avatar">ST</div>
                        <div class="testi-info">
                            <h4>Sai Teja</h4>
                            <span>Verified Customer</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Testimonial 4 -->
            <div class="swiper-slide">
                <div class="testi-card">
                    <div>
                        <div class="testi-stars">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="testi-text">"Very affordable and genuine moving company. They made my relocation completely stress-free and handled the heavy lifting with ease."</p>
                    </div>
                    <div class="testi-author">
                        <div class="testi-avatar">LC</div>
                        <div class="testi-info">
                            <h4>L. Sekhar Chandra</h4>
                            <span>Verified Customer</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Testimonial 5 -->
            <div class="swiper-slide">
                <div class="testi-card">
                    <div>
                        <div class="testi-stars">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="testi-text">"Exceptional teamwork! They packed everything securely and re-assembled my furniture perfectly at the new destination."</p>
                    </div>
                    <div class="testi-author">
                        <div class="testi-avatar">SR</div>
                        <div class="testi-info">
                            <h4>Seenu Royal</h4>
                            <span>Verified Customer</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="swiper-pagination"></div>
    </div>
</section>

<script src="https://unpkg.com/swiper@8/swiper-bundle.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        var swiper = new Swiper(".swiper-testimonials", {
            slidesPerView: 1,
            spaceBetween: 30,
            loop: true,
            autoplay: {
                delay: 3500,
                disableOnInteraction: false,
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                    spaceBetween: 30,
                },
                1024: {
                    slidesPerView: 3,
                    spaceBetween: 40,
                },
            },
        });
    });
</script>
<!-- END CUSTOM TESTIMONIALS SLIDER -->
"""

content = open('index.html', encoding='utf-8').read()

# Replace the specific section with data-id="4a0ec87"
# We match everything from <section class="..." data-id="4a0ec87"... to the matching </section>
# Note: HTML section might contain nested sections, but usually Elementor sections don't nest like this unless inner sections.
# Let's use a trick: match up to the end of the TrustIndex widget and then the closing </section>
pattern = r'<section class="elementor-section[^>]*data-id="4a0ec87".*?trustindex-google-widget.*?</section>'
import re
new_content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Testimonials replaced successfully!")
