import requests
from bs4 import BeautifulSoup
import urllib

# URL of the product page
url = "https://www.flipkart.com/qz-4k-60hz-9-1-usb-c-hub-hdmi-4k-60hz-type-c-dock-laptop-docking-station-qzhb72-usb/p/itmfbe923a0d075c?pid=USGH58G4N6ZSDXEQ&lid=LSTUSGH58G4N6ZSDXEQXWWXTA&marketplace=FLIPKART&q=qz+hub&store=6bo&srno=s_1_13&otracker=search&otracker1=search&fm=Search&iid=cf28d2cd-62d9-4190-8a32-ccce1cab8409.USGH58G4N6ZSDXEQ.SEARCH&ppt=sp&ppn=sp&ssid=5l3bssjg2o0000001735748175987&qH=f8ad4d01973bb839"

# Set headers to mimic a browser
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
# }

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