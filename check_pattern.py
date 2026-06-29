import os
import re

html_path = 'd:/hompage/publication.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Try to match the strict pattern for extraction
li_pattern = r'<li[^>]*>\s*<a href="([^"]*)" target="_blank" class="pub-link">([\s\S]*?)<i class="journal">([\s\S]*?)</i>\s*<span class="year">(\d{4})</span>([\s\S]*?)</a>\s*</li>'
matches = re.findall(li_pattern, html)
print('Total matches with strict pattern:', len(matches))

li_loose = r'(<li[^>]*>\s*<a href="[^"]*" target="_blank" class="pub-link">[\s\S]*?<span class="year">\d{4}</span>[\s\S]*?</a>\s*</li>)'
loose_matches = re.findall(li_loose, html)
print('Total loose matches:', len(loose_matches))
