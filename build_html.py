import os
import re

html_path = 'd:/hompage/publication.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract ALL <li> items from the document
# This avoids any structural nesting issues from previous errors.
li_pattern = r'(<li[^>]*>\s*<a href="[^"]*" target="_blank" class="pub-link">[\s\S]*?<span class="year">(\d{4})</span>[\s\S]*?</a>\s*</li>)'
all_lis = re.findall(li_pattern, html)

papers_by_year = {}
for li_html, year_str in all_lis:
    year = int(year_str)
    if year not in papers_by_year:
        papers_by_year[year] = []
    # Avoid duplicates if previous script caused duplicate <li> blocks
    if li_html not in papers_by_year[year]:
        papers_by_year[year].append(li_html)

# 2. Build new publications container content
new_container = []
new_container.append('''
                <div class="tabs-container" style="display: flex; gap: 10px; margin-bottom: 30px; justify-content: center; flex-wrap: wrap;">
                    <button class="tab-btn active" data-target="2026" style="padding: 8px 20px; border: none; border-radius: 20px; background: #0033A0; color: white; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2026</button>
                    <button class="tab-btn" data-target="2025" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2025</button>
                    <button class="tab-btn" data-target="2024" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2024</button>
                    <button class="tab-btn" data-target="2023" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">2023</button>
                    <button class="tab-btn" data-target="before-archive" style="padding: 8px 20px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif;">Before 2023</button>
                </div>''')

# For 2026 to 2023
for y in [2026, 2025, 2024, 2023]:
    display_style = '' if y == 2026 else ' style="display: none;"'
    active_class = ' active' if y == 2026 else ''
    
    new_container.append(f'''
                    <div id="{y}" class="tab-content{active_class}"{display_style}>
                        <ul class="publication-list pub-list">''')
    for li in papers_by_year.get(y, []):
        new_container.append(f"                            {li}")
    new_container.append('''                        </ul>
                    </div>''')

# For before-archive
new_container.append('''
                    <div id="before-archive" class="tab-content" style="display: none;">''')

for y in range(2022, 2008, -1):
    if y in papers_by_year and papers_by_year[y]:
        new_container.append(f'''
                        <div class="year-section">
                            <h3 class="year-title">{y}</h3>
                            <ul class="publication-list pub-list">''')
        for li in papers_by_year[y]:
            new_container.append(f"                                {li}")
        new_container.append('''                            </ul>
                        </div>''')

new_container.append('''                    </div>''')

# 3. Assemble the full HTML
# Part 1: From start to `<div class="publications-container">`
pub_container_start = html.find('<div class="publications-container">')
if pub_container_start == -1:
    raise Exception("Could not find publications-container")
part1 = html[:pub_container_start + len('<div class="publications-container">')]

# Part 2: New container content
part2 = '\n'.join(new_container)

# Part 3: Footer part. Need to find `</section>` and extract to end, then prepend the two closing divs.
section_end = html.find('        </section>')
if section_end == -1:
    section_end = html.find('</section>')

part3 = '\n                </div>\n            </div>\n' + html[section_end:]

final_html = part1 + part2 + part3

with open('d:/hompage/publication_fixed.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Total papers processed: {sum(len(v) for v in papers_by_year.values())}")
print("Done writing publication_fixed.html")
