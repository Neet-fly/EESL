import bs4

with open('member.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

tabs = soup.find('div', class_='tabs-container')
alumni = soup.find('div', id='alumni')
current = soup.find('div', id='current-members')

if tabs and alumni and current:
    # 1. Unpack current from header
    header = soup.find('header')
    header_container = header.find('div', class_='container header-content')
    tabs.extract()
    alumni.extract()
    
    # extract everything inside current and put it back to header_container
    for child in list(current.children):
        header_container.append(child.extract())
    current.extract()
    
    # 2. Put tabs and alumni in the correct main container
    main_container = soup.find('main').find('div', class_='container')
    
    # find where Ph.D. Students h2 is
    children = list(main_container.children)
    start_idx = 0
    for i, c in enumerate(children):
        if c.name == 'h2' and 'Ph.D.' in c.text:
            start_idx = i
            break
            
    nodes_to_wrap = children[start_idx:]
    new_current = soup.new_tag('div', id='current-members', **{'class': 'tab-content active'})
    for n in nodes_to_wrap:
        new_current.append(n.extract())
        
    # We want tabs at the top of the main container, then new_current, then alumni
    # Wait, they should be before new_current
    main_container.append(tabs)
    main_container.append(new_current)
    main_container.append(alumni)
    
# Fix the navigation links manually for ALL html files
import glob
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # replace Member with Members
    html = html.replace('>Member</a>', '>Members</a>')
    # remove Alumni nav link completely (with its li)
    import re
    html = re.sub(r'<li[^>]*>\s*<a[^>]*href="alumni\.html"[^>]*>Alumni</a>\s*</li>', '', html)
    html = re.sub(r'<a[^>]*href="alumni\.html"[^>]*>Alumni</a>', '', html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

with open('member.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify(formatter="html"))
print("Fixed structure and nav")
