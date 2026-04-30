import requests
from bs4 import BeautifulSoup


r = requests.get("https://chewiecookies.com.br")
html = r.text

soup = BeautifulSoup(html, "html.parser")