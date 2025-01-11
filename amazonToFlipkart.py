from bs4 import BeautifulSoup
import requests
import time

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
    search_url = f"https://www.flipkart.com/search?q={requests.utils.quote(product_name)}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/'
    }
    
    session = requests.Session()
    print(search_url);
    # response = session.get(search_url, headers=headers)

    
    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     print(soup)
    #     # product_link = soup.find('a', class_='_1fQZEK')
    #     products = soup.find_all("a",class_='CGtC98')
    #     # print(products);
    #     # print(products[0]);
    #     print(products[0].get_text())
    #     ref = products[0].get('href')
    #     print("ref", ref)
    #     # if product_link:
    #     #     flipkart_link = "https://www.flipkart.com" + product_link['href']
    #     #     print("Flipkart Link: ", flipkart_link)
    #     #     return flipkart_link
    #     # else:
    #     #     print("Product link not found on Flipkart.")
    #     #     return None
    # else:
    #     print(f"Failed to fetch the page. Status code: {response.status_code}")
    #     return None

# Example usage
amazon_url = "https://www.amazon.in/SAMSUNG-Galaxy-S23-Graphite-Storage/dp/B0CJXQX3MB?th=1"
product_name, product_price = fetch_amazon_product_details(amazon_url)
if product_name:
    search_flipkart(product_name)

# Introduce a delay to avoid being flagged as a bot
time.sleep(2)
