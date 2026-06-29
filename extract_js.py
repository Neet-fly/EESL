import os
import re
import json

html_path = 'd:/hompage/publication.html'
js_path = 'd:/hompage/publications.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

li_pattern = r'<li[^>]*>\s*<a href="([^"]*)" target="_blank" class="pub-link">([\s\S]*?)<i class="journal">([\s\S]*?)</i>\s*<span class="year">(\d{4})</span>([\s\S]*?)</a>\s*</li>'
matches = re.findall(li_pattern, html)

publications = []
for m in matches:
    publications.append({
        "year": int(m[3].strip()),
        "link": m[0].strip(),
        "authorsAndTitle": m[1].strip(),
        "journal": m[2].strip(),
        "details": m[4].strip()
    })

js_content = "const publicationsData = " + json.dumps(publications, ensure_ascii=False, indent=4) + ";\n"

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Extracted {len(publications)} publications to js")

# Refactor HTML:
# 1. Clean the lists for 2026, 2025, 2024, 2023
html = re.sub(r'<ul class="publication-list pub-list">[\s\S]*?</ul>', r'<ul class="publication-list pub-list"></ul>', html)

# 2. Clean the before-archive completely.
start_str = '<div id="before-archive" class="tab-content" style="display: none;">'
before_archive_start = html.find(start_str)

# Find the end of before-archive which is right before the </div> closing publications-container
# The HTML ends with:
#                     </div>
#                 </div>
#             </div>
#         </section>
# Let's search for `</div>\n            </div>\n        </section>` which closes the `publications-container` and `container`
section_end_idx = html.find('</div>\n            </div>\n        </section>')

if section_end_idx != -1:
    # Go back one </div> to find the closing of before-archive
    container_end = html.rfind('</div>', before_archive_start, section_end_idx)
    # So container_end points to the </div> that closes publications-container
    html = html[:before_archive_start] + start_str + '\n                    </div>\n                ' + html[container_end:]
else:
    print("Warning: could not find section_end_idx, attempting alternative fallback")
    html = re.sub(r'(<div id="before-archive" class="tab-content" style="display: none;">)[\s\S]*?(?=</div>\s*</div>\s*</div>\s*</section>)', r'\1\n                    </div>\n                ', html)

# 3. Add publications.js script
if '<script src="publications.js"></script>' not in html:
    html = html.replace('<script src="script.js"></script>', '<script src="publications.js"></script>\n    <script src="script.js"></script>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Finished rewriting HTML")
