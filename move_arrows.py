import re

with open('d:\\hompage\\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change overflow: hidden to overflow: visible in .slider-container
content = re.sub(
    r'(\.slider-container\s*\{[^}]*)overflow:\s*hidden;([^}]*\})',
    r'\1overflow: visible;\2',
    content
)

# 2. Add border-radius to .slide-img
content = re.sub(
    r'(\.slide-img\s*\{[^}]*)object-fit:\s*cover;([^}]*\})',
    r'\1object-fit: cover;\n    border-radius: 12px;\2',
    content
)

# 3. Move .prev-btn outside
content = re.sub(
    r'(\.prev-btn\s*\{\s*)left:\s*15px;\s*\}',
    r'\1left: -60px;\n}',
    content
)

# 4. Move .next-btn outside
content = re.sub(
    r'(\.next-btn\s*\{\s*)right:\s*15px;\s*\}',
    r'\1right: -60px;\n}',
    content
)

with open('d:\\hompage\\style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Slider arrows moved outside.")
