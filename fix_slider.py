import re

with open('d:\\hompage\\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the slider-container block
old_block = r"""\.slider-container\s*\{[^}]*\}"""
new_block = """.slider-container {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
    width: 100%;
    aspect-ratio: 4 / 3;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    background-color: rgba(255, 255, 255, 0.1);
}"""

content = re.sub(old_block, new_block, content, count=1)

with open('d:\\hompage\\style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed slider-container CSS")
