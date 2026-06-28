import os
import re

html_files = [
    'index.html', 'research.html', 'pi.html', 'member.html', 
    'alumni.html', 'publication.html', 'news.html', 'contact.html'
]

pattern = re.compile(r'<a href="index\.html" class="logo">\s*<img src="\./images/EESL logo\.png" alt="EESL Logo">\s*</a>')

replacement = '''<a href="index.html" class="logo-container">
            <img src="./images/EESL logo.png" alt="EESL Logo" class="header-logo-img">
            <div class="logo-text-group">
                <span class="logo-main-text">EESL</span>
                <span class="logo-sub-text">Electrochemical Energy Storage Lab</span>
            </div>
        </a>'''

for f in html_files:
    path = os.path.join('d:\\hompage', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = pattern.sub(replacement, content)
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
    else:
        print(f"Skipped {f} (not found)")

css_addition = """

/* --- New Logo Container Styles --- */
.logo-container {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
}
.header-logo-img {
    height: 40px; 
    width: auto;
}
.logo-text-group {
    display: flex;
    flex-direction: column;
    justify-content: center;
    line-height: 1.2;
}
.logo-main-text {
    font-size: 1.4rem;
    font-weight: 800;
    color: var(--primary-color, #003399);
    letter-spacing: 0.5px;
}
.logo-sub-text {
    font-size: 0.75rem;
    font-weight: 500;
    color: #555555;
    white-space: nowrap; 
}

@media (max-width: 768px) {
    .logo-sub-text {
        display: none;
    }
}
"""

with open('d:\\hompage\\style.css', 'a', encoding='utf-8') as file:
    file.write(css_addition)
print("Updated style.css")
