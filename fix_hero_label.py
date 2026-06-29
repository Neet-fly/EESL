import bs4

with open('index.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

label = soup.find('div', class_='hero-label')
if label:
    label.clear()
    label.append("Yonsei University ")
    
    dot = soup.new_tag('span', **{'class': 'hero-dot'})
    dot.string = "·"
    label.append(dot)
    
    br = soup.new_tag('br', **{'class': 'hero-br'})
    label.append(br)
    
    label.append(" Materials Science & Engineering")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Fixed hero label in index.html")
