css = """

/* --- Premium Hero Redesign --- */
.hero {
  min-height: 650px;
  padding: 110px 7% 90px;
  display: grid !important; 
  grid-template-columns: 1fr 1.05fr !important;
  align-items: center;
  gap: 70px;
  background: linear-gradient(135deg, #0b2f78 0%, #123f9d 100%) !important;
  color: #ffffff;
}
.hero-content { max-width: 620px; }
.hero-label {
  display: inline-block;
  margin-bottom: 22px;
  padding: 8px 14px;
  border: 1px solid rgba(255, 255, 255, 0.22);
  border-radius: 999px;
  color: #d7e5ff;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.02em;
  background: rgba(255, 255, 255, 0.06);
}
.hero h1 {
  margin: 0;
  font-size: clamp(40px, 4.5vw, 68px) !important;
  line-height: 1.1;
  letter-spacing: -0.04em;
  font-weight: 800;
}
.hero h1 span { color: #ffcc2f; }
.hero-subtitle {
  margin-top: 28px;
  max-width: 560px;
  color: #e5edff;
  font-size: 19px !important;
  line-height: 1.65;
  font-weight: 400;
}
.hero-buttons { display: flex; gap: 14px; margin-top: 36px; }
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 14px 24px;
  border-radius: 999px;
  font-size: 15px;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.2s ease;
}
.btn.primary { background: #ffcc2f; color: #0b2f78; }
.btn.secondary { border: 1px solid rgba(255, 255, 255, 0.35); color: #ffffff; background: rgba(255, 255, 255, 0.08); }
.btn:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }

/* 이미지 프레임 고급화 */
.hero-image-wrap {
  position: relative;
  border-radius: 22px;
  padding: 10px;
  background: rgba(255, 255, 255, 0.12);
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.28);
  overflow: hidden;
  aspect-ratio: 4 / 3;
}
.hero-image-wrap img {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 16px;
  object-fit: cover;
}
.image-caption {
  position: absolute;
  left: 24px;
  bottom: 24px;
  padding: 10px 16px;
  border-radius: 999px;
  color: #ffffff;
  font-size: 13px;
  font-weight: 600;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 12;
}

@media (max-width: 768px) {
  .hero {
    display: flex !important;
    flex-direction: column !important;
    padding: 120px 5% 50px !important;
    gap: 40px !important;
  }
  .hero-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .hero h1 {
    font-size: clamp(32px, 8vw, 42px) !important;
  }
  .hero-buttons {
    justify-content: center;
  }
  .image-caption {
    left: 14px;
    bottom: 14px;
    font-size: 11px;
    padding: 6px 12px;
  }
}
"""

with open('d:\\hompage\\style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Premium Hero CSS injected successfully.")
