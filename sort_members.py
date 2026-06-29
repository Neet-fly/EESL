import bs4
import re

with open("d:/hompage/member.html", "r", encoding="utf-8") as f:
    soup = bs4.BeautifulSoup(f, "html.parser")

phd_list = soup.find_all("div", class_="members-list")[0]
ms_list = soup.find_all("div", class_="members-list")[1]

# Collect all member cards from both lists
all_cards = phd_list.find_all("div", class_="member-card", recursive=False) + ms_list.find_all("div", class_="member-card", recursive=False)

# Clear both lists
phd_list.clear()
ms_list.clear()

phd_count = 1
ms_count = 1

for card in all_cards:
    course_text = card.find(string=re.compile("COURSE:")).parent.parent.text
    if "Ph.D." in course_text:
        # Update the comment (optional, but good for cleanliness)
        # Actually BS4 strips comments if we just manipulate, but let's just append the card
        phd_list.append(card)
        phd_count += 1
    else:
        ms_list.append(card)
        ms_count += 1

with open("d:/hompage/member.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"Moved {phd_count-1} to PhD, {ms_count-1} to MS")
