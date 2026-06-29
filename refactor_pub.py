import os
import re

html_path = 'd:/hompage/publication.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Clean up stray </div> after 2022 tab
extra_div_pattern = r'(<div id="2022" class="tab-content" style="display: none;">[\s\S]*?</ul>\s*</div>)\s*</div>'
html = re.sub(extra_div_pattern, r'\1', html)

# Replace Tabs Container
old_tabs_pattern = r'<div class="tabs-container".*?</div>'
new_tabs = '''<div class="tabs-container" style="display: flex; gap: 10px; margin-bottom: 30px; justify-content: center; flex-wrap: wrap;">
                    <button class="tab-btn active" data-target="2026" style="padding: 8px 20px; border: none; border-radius: 20px; background: #0033A0; color: white; cursor: pointer; font-weight: 600; font-family: \'Inter\', sans-serif;">2026</button>
                    <button class="tab-btn" data-target="2025" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: \'Inter\', sans-serif;">2025</button>
                    <button class="tab-btn" data-target="2024" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: \'Inter\', sans-serif;">2024</button>
                    <button class="tab-btn" data-target="2023" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: \'Inter\', sans-serif;">2023</button>
                    <button class="tab-btn" data-target="before-archive" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: \'Inter\', sans-serif;">Before 2023</button>
                </div>'''
html = re.sub(old_tabs_pattern, new_tabs, html, flags=re.DOTALL)

# Extract contents of 2022 to 2009
years = ["2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2011", "2010", "2009"]
archive_html_parts = []

for y in years:
    pattern = r'<div id="' + y + r'" class="tab-content".*?<ul class="publication-list pub-list">([\s\S]*?)</ul>\s*</div>'
    match = re.search(pattern, html, flags=re.DOTALL)
    if match:
        ul_content = match.group(1).strip()
        archive_html_parts.append(f'''                    <div class="year-section">
                        <h3 class="year-title">{y}</h3>
                        <ul class="publication-list pub-list">
                            {ul_content}
                        </ul>
                    </div>''')
        html = html.replace(match.group(0), "")
    else:
        print(f"Warning: Could not find tab {y}")

# Create before-archive div
before_archive_content = '''
                    <div id="before-archive" class="tab-content" style="display: none;">
''' + '\n\n'.join(archive_html_parts) + '''
                    </div>'''

# Insert before-archive right after 2023 div ends
pattern_2023 = r'<div id="2023" class="tab-content".*?</ul>\s*</div>'
match_2023 = re.search(pattern_2023, html, flags=re.DOTALL)
if match_2023:
    end_index = match_2023.end()
    html = html[:end_index] + '\n' + before_archive_content + html[end_index:]
else:
    print("Error: Could not find 2023 div")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
