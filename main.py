from bs4 import BeautifulSoup
import requests

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
        else:
            print("Title section not found.")
            return None, None
        
        price_section = soup.find('span', id="tp_price_block_total_price_ww")
        if price_section:
            product_price = price_section.text.strip()
        else:
            print("Price not found.")
            product_price = None
        
        return product_title, product_price
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None, None
    
def get_flipkart_product_details(url):

    response = requests.get(url)
    if response.status_code == 200:     
        soup = BeautifulSoup(response.text,'html.parser')
        title = soup.find('h1').text.strip().replace("/", "").replace("[", "").replace("]", "")
        pricing = soup.find("div", {"class": "hl05eU"}).text.strip()
        cleaned_price = pricing.lstrip("₹")
        price_parts = cleaned_price.split("₹")
        price = price_parts[0].replace(",", "")
        return title,price
    
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")


