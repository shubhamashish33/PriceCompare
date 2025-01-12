import time
import requests
from bs4 import BeautifulSoup
import urllib

from amazonToFlipkart import fetch_amazon_product_details

# URL of the product page

def flipkart_to_amazon(url):
    # Make a GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.text,'html.parser')

        title = soup.find('h1').text.strip().replace("/", "").replace("[", "").replace("]", "")
        encoded_query = urllib.parse.quote_plus(title)

        print(f"Product Name : {encoded_query}")

        pricing = soup.find("div", {"class": "hl05eU"}).text.strip()

        cleaned_price = pricing.lstrip("₹")

        # Split the string at the first occurrence of the numeric value
        price_parts = cleaned_price.split("₹")

        # Get the first part and remove any commas
        price = price_parts[0].replace(",", "")

        print(f"Price: {price}")

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")


    # Format search URL for Amazon
    amazon_url = f"https://www.amazon.in/s/ref=nb_sb_noss?field-keywords={encoded_query}"

    print(f"Amazon URL: {amazon_url}")

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
        # print(soup)  
        # Extract product titles from the search results
        products = soup.find_all("a", class_="a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal")
        ref = products[0].get('href')
        link=f"https://www.amazon.in{ref}"
        print(link)
        time.sleep(2)

        value = fetch_amazon_product_details(link)
        # for product in products[:5]:  # Limit to first 5 results
        #     print(product.get_text())
    else:
        print(f"Failed to fetch Amazon search results. Status code: {response.status_code}")
    

productLink = "https://www.flipkart.com/redmi-a4-5g-only-jio-sim-sparkle-purple-128-gb/p/itmf6a8b6a3d4395?pid=MOBH6YHDGD57AVHX&lid=LSTMOBH6YHDGD57AVHXCXID0O&marketplace=FLIPKART&q=Redmi+A4+5G&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=15869eca-b36c-4c06-a5a9-4f8f5986bc88.MOBH6YHDGD57AVHX.SEARCH&ppt=pp&ppn=pp&ssid=nx4o205vz40000001736628498934&qH=422401bae45a578b"
flipkart_to_amazon(productLink)