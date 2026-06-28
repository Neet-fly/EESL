css = """

/* --- Hero Height & Slider Fixes --- */
.hero {
  min-height: calc(100vh - 90px) !important;
}

.hero-image-wrap .slide-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.5s ease;
  z-index: 0;
  object-fit: cover;
  border-radius: 16px;
}

.hero-image-wrap .slide-img.active {
  opacity: 1;
  z-index: 1;
}

.hero-image-wrap .slider-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 20 !important;
  background: rgba(0, 0, 0, 0.4);
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-radius: 50%;
  font-size: 1.2rem;
  transition: background 0.3s;
}

.hero-image-wrap .slider-btn:hover {
  background: rgba(0, 0, 0, 0.7);
}

.hero-image-wrap .prev-btn {
  left: 15px !important;
}

.hero-image-wrap .next-btn {
  right: 15px !important;
}
"""

with open('d:\\hompage\\style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Hero height and slider fixes injected successfully.")
