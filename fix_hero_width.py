with open('d:\\hompage\\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    ".hero-image {\n    display: flex;",
    ".hero-image {\n    display: flex;\n    width: 100%;"
)

with open('d:\\hompage\\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
print("hero-image width fixed")
