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

    #with open("output.html", "w", encoding="utf-8") as file:
    # file.write(response.text)

    # Parse HTML
    soup = BeautifulSoup(response.content, "lxml")

    # Extract Data (Note: Amazon IDs can change, so these may need updates)
    data = {}
    try:
        data['title'] = soup.find("span", attrs={"id": 'productTitle'}).get_text(strip=True)
        data['price'] = soup.find("span", attrs={"class": 'a-offscreen'}).get_text(strip=True)
        data['rating'] = soup.find("span", attrs={"class": 'a-icon-alt'}).get_text(strip=True)
        review_elements = soup.find_all('li', {'data-hook': 'review'})
        extracted_reviews = []
        for review in review_elements:
            review_item = {
                'id': review.get('id'),
                'title': review.find('a', {'data-hook': 'review-title'}).get_text(strip=True) if review.find('a', {'data-hook': 'review-title'}) else None,
                'rating': review.find('i', {'data-hook': 'review-star-rating'}).get_text(strip=True) if review.find('i', {'data-hook': 'review-star-rating'}) else None,
                'body': review.find('span', {'data-hook': 'review-body'}).get_text(strip=True) if review.find('span', {'data-hook': 'review-body'}) else None
            }
            extracted_reviews.append(review_item)
            
        data['reviews'] = extracted_reviews
    except AttributeError:
        print("Could not find some elements. Amazon might have blocked the request or changed layout.")
    
    return data

# Example Usage
product_url = "https://www.amazon.com/dp/B0CMZ46PHR"
print(get_amazon_product(product_url))