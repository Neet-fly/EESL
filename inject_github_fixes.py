css = """

/* --- Github Layout Break Fixes --- */
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow-x: hidden;
}

.hero-slider-outer {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.hero-slider-outer .slider-btn {
  position: absolute;
  z-index: 30 !important;
  background: rgba(255, 255, 255, 0.2) !important;
  width: 44px !important;
  height: 44px !important;
  border-radius: 50% !important;
  color: white !important;
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.2rem;
  transition: all 0.3s ease !important;
}

.hero-slider-outer .slider-btn:hover {
  background: #ffcc2f !important;
  color: #0b2f78 !important;
  border-color: #ffcc2f !important;
}

.hero-slider-outer .prev-btn {
  left: -50px !important;
}

.hero-slider-outer .next-btn {
  right: -50px !important;
}

.hero {
  min-height: calc(100vh - 90px) !important;
  box-sizing: border-box !important;
  display: grid !important;
  grid-template-columns: 1fr 1.1fr !important;
  gap: 60px !important;
}

.hero-image-wrap {
  width: 100% !important;
  max-width: 540px !important;
  aspect-ratio: 4 / 3 !important;
  position: relative !important;
  border-radius: 22px !important;
  padding: 10px !important;
  background: rgba(255, 255, 255, 0.12) !important;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.28) !important;
  overflow: hidden !important;
}

@media (max-width: 768px) {
  .hero {
    display: flex !important;
    flex-direction: column !important;
  }
  .hero-slider-outer .prev-btn {
    left: -15px !important;
  }
  .hero-slider-outer .next-btn {
    right: -15px !important;
  }
}
"""

with open('d:\\hompage\\style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Github Layout Break Fixes injected successfully.")
