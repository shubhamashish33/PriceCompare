import requests
from bs4 import BeautifulSoup
import urllib

# URL of the product page
url = "https://www.flipkart.com/cmf-nothing-100-w-power-gan-5-3-port-mobile-charger-detachable-cable/p/itm2f0f45bd04629?pid=ACCH4H7AJHNEYNXA&lid=LSTACCH4H7AJHNEYNXAFF4GNF&marketplace=FLIPKART&q=cmf+charger&store=tyy%2F4mr%2Ftp2&srno=s_1_4&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&fm=search-autosuggest&iid=f179953f-388b-48e4-8ce3-c70e78455de0.ACCH4H7AJHNEYNXA.SEARCH&ppt=sp&ppn=sp&ssid=p4iffod0dc0000001735569958496&qH=f36109ce0fe857e2"

# Set headers to mimic a browser
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
# }

# Make a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    
    soup = BeautifulSoup(response.text,'html.parser')

    title = soup.find('h1').text.strip().replace("/", "")
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

print(amazon_url)

response = requests.get(amazon_url)

# Parse the results
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")  
    # print(soup)  
    # Extract product titles from the search results
    products = soup.find_all("a", class_="a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal")
    print(products[0].get_text())
    ref = products[0].get('href')
    print(f"https://www.amazon.in{ref}")
    # for product in products[:5]:  # Limit to first 5 results
    #     print(product.get_text())
else:
    print(f"Failed to fetch Amazon search results. Status code: {response.status_code}")