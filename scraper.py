import requests
from bs4 import BeautifulSoup
import json


# this code get the brand's menu and return all items with their respective prices
URL = "https://chewiecookies.com.br"

def fetch_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        print("Error:", e)


def parse_html(html):
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")

    items = []
    for item in soup.find_all(class_ = "item-produto"):
        '''get the name and the price'''
        name_tag = item.find("h3")
        price_tag = item.find("strong")

        if name_tag and price_tag:
            items.append({
                "name" : name_tag.get_text(strip=True),
                "price" : price_tag.get_text(strip=True)
            })
    
    return items


def save_html(items):
    with open("items.json", "w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    html = fetch_html(URL)
    items = parse_html(html)
    save_html(items)