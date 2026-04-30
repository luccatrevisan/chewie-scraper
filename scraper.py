import requests
from bs4 import BeautifulSoup
import json


# this code get the brand's menu and return all items with their respective prices
r = requests.get("https://chewiecookies.com.br")
html = r.text

soup = BeautifulSoup(html, "html.parser")


items = []
for item in soup.find_all(class_ = "item-produto"):
    '''get the name and the price'''
    name = item.h3.text
    price = item.strong.text

    items.append({
        "name" : name.strip(),
        "price" : price.strip()
    })

print(items)

# with open("items.json", "w", encoding="utf-8") as file:
#    json.dump(items, file, ensure_ascii=False, indent=2)