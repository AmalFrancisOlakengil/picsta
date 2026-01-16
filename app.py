import requests
from bs4 import BeautifulSoup

url = "https://www.instagram.com/p/DSxQ85CCKJh/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()   # raises error if request failed

html = response.text

soup = BeautifulSoup(html, "lxml")

div = soup.find("div", class_="_aagv")
img = div.find("img")

image_url = img.get("src") or img.get("data-src")

print(image_url)


