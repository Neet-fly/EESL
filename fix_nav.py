import glob
import bs4

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    # 1. Rename Member -> Members in the nav link
    # Find a tag with href="member.html"
    member_link = soup.find('a', href='member.html')
    if member_link:
        # Sometimes the text might have extra spaces or newlines
        member_link.string = "Members"
        
    # 2. Remove Alumni from nav list
    alumni_link = soup.find('a', href='alumni.html')
    if alumni_link:
        # Find the parent li and remove it entirely
        parent_li = alumni_link.find_parent('li')
        if parent_li:
            parent_li.decompose()
        else:
            alumni_link.decompose()
            
    with open(file, 'w', encoding='utf-8') as f:
        # Just write the string back, avoid prettify if it wasn't prettified
        # But for member.html, it's already prettified.
        # Actually, using str(soup) is best to avoid crazy whitespace changes.
        f.write(str(soup))
print("Nav fixed globally.")
