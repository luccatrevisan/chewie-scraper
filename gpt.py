import requests
from bs4 import BeautifulSoup
import json

URL = "https://example.com"  # substitua por um site real

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text
    

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    items = []

    for article in soup.select("article"):
        title = article.select_one("h2")
        link = article.select_one("a")

        items.append({
            "title": title.text.strip() if title else None,
            "link": link["href"] if link else None
        })

    return items

def save(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    html = fetch_page(URL)
    data = parse(html)
    save(data)