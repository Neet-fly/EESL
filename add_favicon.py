import glob

html_files = glob.glob('d:\\hompage\\*.html')

favicon_code = """    <link rel="icon" href="./images/favicon.png" type="image/png">
    <link rel="apple-touch-icon" href="./images/favicon.png">
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        content = content.replace('</head>', f'{favicon_code}</head>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Favicon added to all HTML files.")
