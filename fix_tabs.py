import re

with open('d:/hompage/publication.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Generate tabs
tabs_html = '''
                <div class="tabs-container" style="display: flex; gap: 10px; margin-bottom: 30px; justify-content: center; flex-wrap: wrap;">
                    <button class="tab-btn active" data-target="2026" style="padding: 8px 20px; border: none; border-radius: 20px; background: #0033A0; color: white; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2026</button>
                    <button class="tab-btn" data-target="2025" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2025</button>
                    <button class="tab-btn" data-target="2024" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2024</button>
                    <button class="tab-btn" data-target="2023" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2023</button>
                    <button class="tab-btn" data-target="2022" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2022</button>
                    <button class="tab-btn" data-target="2021" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2021</button>
                    <button class="tab-btn" data-target="2020" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2020</button>
                </div>
'''

if 'tabs-container' not in content:
    content = content.replace('<div class="publications-container">', '<div class="publications-container">\n' + tabs_html)

# Replace year-section
def replace_year(match):
    year = match.group(1)
    active_class = ' active' if year == '2026' else ''
    style = '' if year == '2026' else ' style="display: none;"'
    return f'<div id="{year}" class="tab-content{active_class}"{style}>\n                        <ul class="publication-list pub-list">'

content = re.sub(r'<div class="year-section">\s*<h3 class="year-title">(\d{4})</h3>\s*<ul class="publication-list">', replace_year, content)

with open('d:/hompage/publication.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('d:/hompage/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

if 'tab-btn' not in js_content:
    tab_js = '''
    // Publication Tabs Toggle
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    if (tabBtns.length > 0 && tabContents.length > 0) {
        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active classes
                tabBtns.forEach(b => {
                    b.classList.remove('active');
                    b.style.background = '#e0e0e0';
                    b.style.color = '#333';
                });
                tabContents.forEach(content => {
                    content.classList.remove('active');
                    content.style.display = 'none';
                });

                // Add active class to clicked
                btn.classList.add('active');
                btn.style.background = '#0033A0';
                btn.style.color = 'white';
                
                const targetId = btn.getAttribute('data-target') || btn.textContent.trim();
                const targetContent = document.getElementById(targetId);
                if (targetContent) {
                    targetContent.classList.add('active');
                    targetContent.style.display = 'block';
                }
            });
        });
    }
'''
    js_content += tab_js
    with open('d:/hompage/script.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
