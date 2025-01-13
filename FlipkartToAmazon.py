import time
import requests
from bs4 import BeautifulSoup
import urllib

from main import fetch_amazon_product_details, get_flipkart_product_details

def fetch_amazon_product(title):
    
    encoded_query = urllib.parse.quote_plus(title)
    amazon_url = f"https://www.amazon.in/s/ref=nb_sb_noss?field-keywords={encoded_query}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/'
    }

    response = requests.get(amazon_url, headers=headers)
    time.sleep(2)

    # Parse the results
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")  
        products = soup.find_all("a", class_="a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal")
        for product in products:
            ref=product.get("href")
            if ref.startswith("/sspa/"): # Sponsored products filter out
                continue
            else:
                link=f"https://www.amazon.in{ref}"
                amzn_title,amzn_price = fetch_amazon_product_details(link)
                return amzn_title,amzn_price
    else:
        print(f"Failed to fetch Amazon search results. Status code: {response.status_code}")

if __name__ == "__main__":
    # URL of the product page
    productLink = "https://www.flipkart.com/logitech-mx-master-3s-wireless-touch-mouse/p/itm271ade01ff274?pid=ACCGFPFCAFGREFHZ&lid=LSTACCGFPFCAFGREFHZMWXUSH&marketplace=FLIPKART&q=mx+master+3s&store=6bo%2Fai3%2F2ay&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&fm=search-autosuggest&iid=847c1894-9948-43d8-86be-a7fe149a41a0.ACCGFPFCAFGREFHZ.SEARCH&ppt=sp&ppn=sp&ssid=nq91tj9xkw0000001736691420158&qH=44b100c8bdb752b1"

    flpkrt_title,flpkrt_price = get_flipkart_product_details(productLink)
    print(f"Flipkart Product Name ----> {flpkrt_title}\n")
    print(f"Flipkart Product Price ----> {flpkrt_price}\n")

    amzon_title,amzn_price = fetch_amazon_product(flpkrt_title)
    print(f"Amazon Product Name -----> {amzon_title}\n")
    print(f"Amazon Product Price -----> {amzn_price}\n")

    time.sleep(2)