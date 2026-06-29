import os
import glob
import re
import bs4

# 1. Update Navigation in ALL HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Rename Member to Members
    content = re.sub(r'<a href="member\.html" class="nav-link(\s+active)?">Member</a>', r'<a href="member.html" class="nav-link\1">Members</a>', content)
    
    # Remove Alumni link and its enclosing li
    content = re.sub(r'<li>\s*<a href="alumni\.html" class="nav-link(\s+active)?">Alumni</a>\s*</li>', '', content)
    # Also in case it's not wrapped in li on some lines
    content = re.sub(r'<a href="alumni\.html" class="nav-link(\s+active)?">Alumni</a>', '', content)
    # Remove any empty li that might be left over
    content = re.sub(r'<li>\s*</li>', '', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. M.S.-Ph.D. -> M.S.&Ph.D. in member.html
with open('member.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('M.S.-Ph.D. Integrated Student', 'M.S.&Ph.D. Integrated Student')
with open('member.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 3. Merge Alumni into Member
with open("alumni.html", "r", encoding="utf-8") as f:
    soup_alumni = bs4.BeautifulSoup(f, "html.parser")
alumni_list = soup_alumni.find("div", class_="members-list")

with open("member.html", "r", encoding="utf-8") as f:
    soup_member = bs4.BeautifulSoup(f, "html.parser")

container = soup_member.find("div", class_="container")
children = list(container.children)

start_idx = 0
for i, child in enumerate(children):
    if child.name == 'h2':
        start_idx = i
        break

nodes_to_wrap = children[start_idx:]

current_members_div = soup_member.new_tag("div", id="current-members", **{"class": "tab-content active"})
for node in nodes_to_wrap:
    current_members_div.append(node.extract())

alumni_div = soup_member.new_tag("div", id="alumni", **{"class": "tab-content", "style": "display: none;"})
alumni_title = soup_member.new_tag("h2", **{"class": "section-title"})
alumni_title.string = "Alumni"
alumni_div.append(alumni_title)
alumni_div.append(alumni_list)

tabs_html = """
<div class="tabs-container" style="display: flex; gap: 10px; margin-bottom: 40px; justify-content: center; flex-wrap: wrap;">
    <button class="tab-btn active" data-target="current-members" style="padding: 8px 24px; border: none; border-radius: 20px; background: #0033A0; color: white; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif; font-size: 1.1rem;">Members</button>
    <button class="tab-btn" data-target="alumni" style="padding: 8px 24px; border: none; border-radius: 20px; background: #e0e0e0; color: #333; cursor: pointer; font-weight: 600; font-family: 'Inter', sans-serif; font-size: 1.1rem;">Alumni</button>
</div>
"""
tabs_soup = bs4.BeautifulSoup(tabs_html, "html.parser")

container.append(tabs_soup)
container.append(current_members_div)
container.append(alumni_div)

with open("member.html", "w", encoding="utf-8") as f:
    f.write(str(soup_member))

print("DONE")
