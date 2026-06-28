css = """

/* --- Mobile Hero Overrides --- */
@media (max-width: 768px) {
    .hero-content-grid {
        display: flex;
        flex-direction: column;
        padding: 40px 20px;
        gap: 30px;
    }
    .hero-title {
        font-size: 2.1rem !important;
    }
    .hero-subtitle {
        font-size: 1.05rem !important;
    }
    .hero-text {
        text-align: center;
    }
    .slider-container {
        width: 100% !important;
        max-width: 400px;
        height: 300px !important;
        aspect-ratio: auto !important;
        margin: 0 auto;
    }
    .slider-btn {
        width: 36px !important;
        height: 36px !important;
        font-size: 1rem !important;
    }
    .prev-btn {
        left: 8px !important;
    }
    .next-btn {
        right: 8px !important;
    }
}
"""

with open('d:\\hompage\\style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Appended mobile overrides.")
