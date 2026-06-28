css = """

/* --- Hero Slider Styles --- */
.slider-container {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
    width: 100%;
    height: 100%;
    min-height: 350px;
}
.slider-wrapper {
    position: relative;
    width: 100%;
    height: 100%;
}
.slide-img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0;
    transition: opacity 0.5s ease-in-out;
}
.slide-img.active {
    opacity: 1;
    z-index: 1;
}
.slider-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.3);
    color: white;
    border: none;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.2rem;
    border-radius: 50%;
    transition: background 0.3s ease-in-out;
    z-index: 10;
}
.slider-btn:hover {
    background: rgba(0, 0, 0, 0.7);
}
.prev-btn {
    left: 15px;
}
.next-btn {
    right: 15px;
}
"""

with open('d:\\hompage\\style.css', 'a', encoding='utf-8') as f:
    f.write(css)
print("Slider CSS appended.")
