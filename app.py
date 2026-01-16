import requests
from bs4 import BeautifulSoup
import os

url = "https://medium.com/tag/technology/recommended"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()   # raises error if request failed

html = response.text

# 2. Create the folder if it doesn't exist
folder_name = "html_output"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 3. Define the file path
file_path = os.path.join(folder_name, "index.html")

# 4. Save the variable into the file
with open(file_path, "w") as file:
    file.write(html)

print(f"File saved successfully at: {file_path}")
'''
soup = BeautifulSoup(html, "lxml")
print("_aagv" in html)
div = soup.find("div", class_="_aagv")
img = div.find("img")

image_url = img.get("src") or img.get("data-src")

print(image_url)
'''



