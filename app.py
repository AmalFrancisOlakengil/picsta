import requests
from bs4 import BeautifulSoup

def get_amazon_product(url):
    # Mimic a real browser header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.5"
    }

    # Fetch the page
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return None

    # Parse HTML
    soup = BeautifulSoup(response.content, "lxml")

    # Extract Data (Note: Amazon IDs can change, so these may need updates)
    data = {}
    try:
        data['title'] = soup.find("span", attrs={"id": 'productTitle'}).get_text(strip=True)
        data['price'] = soup.find("span", attrs={"class": 'a-offscreen'}).get_text(strip=True)
        data['rating'] = soup.find("span", attrs={"class": 'a-icon-alt'}).get_text(strip=True)
    except AttributeError:
        print("Could not find some elements. Amazon might have blocked the request or changed layout.")
    
    return data

# Example Usage
product_url = "https://www.amazon.com/dp/B0CMZ46PHR"
print(get_amazon_product(product_url))