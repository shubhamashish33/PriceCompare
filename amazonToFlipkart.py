from bs4 import BeautifulSoup
import requests
import time
import json
from fuzzywuzzy import fuzz

def fetch_amazon_product_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/'
    }
    
    session = requests.Session()
    response = session.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_section = soup.find('span', id='productTitle')
        if title_section:
            product_title = title_section.text.strip()
            print("Product Name: ", product_title)
        else:
            print("Title section not found.")
            return None, None
        
        price_section = soup.find('span', id="tp_price_block_total_price_ww")
        if price_section:
            product_price = price_section.text.strip()
            print("Product Price: ", product_price)
        else:
            print("Price not found.")
            product_price = None
        
        return product_title, product_price
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None, None

def search_flipkart(product_name):
    # Limit the product name to the first two or three words
    limited_product_name = ' '.join(product_name.split()[:3])
    search_url = f"https://www.flipkart.com/search?q={requests.utils.quote(limited_product_name)}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/'
    }
    
    session = requests.Session()
    print("Search URL: ", search_url)
    response = session.get(search_url, headers=headers)
    
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            script_tag = soup.find('script', {'id': 'jsonLD'})
            if script_tag:
                data = json.loads(script_tag.string)
                itemListElement = data.get("itemListElement")
                if itemListElement and len(itemListElement) > 0:
                    best_match = None
                    highest_ratio = 0
                    for item in itemListElement:
                        item_name = item.get('name', '').lower()
                        ratio = fuzz.partial_ratio(limited_product_name.lower(), item_name)
                        if ratio > highest_ratio:
                            highest_ratio = ratio
                            best_match = item
                    if best_match:
                        product_link = best_match.get('url')
                        if product_link:
                            print("\nProduct Link 🔗: ", product_link)
                            return product_link
                    print("Matching product link not found on Flipkart.")
                    return None
                else:
                    print("Product not found in JSON data.")
                    return None
            else:
                print("JSON script tag not found.")
                return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

# Example usage
amazon_url = "https://www.amazon.in/SAMSUNG-Galaxy-S23-Graphite-Storage/dp/B0CJXQX3MB?th=1"
product_name, product_price = fetch_amazon_product_details(amazon_url)
if product_name:
    search_flipkart(product_name)

# Introduce a delay to avoid being flagged as a bot
time.sleep(2)
