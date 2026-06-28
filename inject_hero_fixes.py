css = """

/* --- Extreme layout fixes for Hero --- */
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow-x: hidden;
}

.hero {
  height: calc(100vh - 90px) !important;
  min-height: auto !important;
  box-sizing: border-box !important;
  padding: 0 7% !important;
}

.hero-slider-outer {
  position: relative;
  width: 100%;
}

.hero-slider-outer .slider-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 30 !important;
  background: rgba(255, 255, 255, 0.15) !important;
  color: #ffffff !important;
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
  width: 48px !important;
  height: 48px !important;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-radius: 50%;
  font-size: 1.4rem;
  transition: all 0.3s ease !important;
  backdrop-filter: blur(4px);
}

.hero-slider-outer .slider-btn:hover {
  background: #ffcc2f !important;
  color: #0b2f78 !important;
  border-color: #ffcc2f !important;
}

.hero-slider-outer .prev-btn {
  left: -24px !important;
}

.hero-slider-outer .next-btn {
  right: -24px !important;
}

@media (max-width: 768px) {
  .hero {
    height: auto !important;
    min-height: calc(100vh - 90px) !important;
    padding: 60px 5% 40px !important;
  }
  .hero-slider-outer .prev-btn {
    left: -10px !important;
  }
  .hero-slider-outer .next-btn {
    right: -10px !important;
  }
  .hero-slider-outer .slider-btn {
    width: 36px !important;
    height: 36px !important;
    font-size: 1rem;
  }
}
"""

with open('d:\\hompage\\style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Hero extreme layout fixes injected successfully.")
