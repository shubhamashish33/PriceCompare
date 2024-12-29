import requests
from bs4 import BeautifulSoup

# URL of the product page
url = "https://www.flipkart.com/benq-mx560-4000-lm-1-speaker-remote-controller-dlp-20000-1-high-contrast-ratio-dual-hdmi-usb-a-upto-15000-hrs-extra-long-lamp-life-10w-speaker-3d-capable-xga-business-education-projector/p/itmc2c43606e806a?pid=PROGVP6Z52ZGGGZA&lid=LSTPROGVP6Z52ZGGGZAJ03DQK&marketplace=FLIPKART&q=benq&store=6bo%2Ftia&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=da213a09-c689-46b2-a87a-c6268dd482bb.PROGVP6Z52ZGGGZA.SEARCH&ppt=sp&ppn=sp&ssid=oc96p7988w0000001735497552049&qH=eacf6d16adf5c83d"

# Set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}

# Make a GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    
    soup = BeautifulSoup(response.text,'html.parser')

    title = soup.find('h1').text.strip()

    print(f"Product Name : {title}")

    pricing = soup.find("div", {"class": "hl05eU"}).text.strip()

    cleaned_price = pricing.lstrip("₹")

    # Split the string at the first occurrence of the numeric value
    price_parts = cleaned_price.split("₹")

    # Get the first part and remove any commas
    price = price_parts[0].replace(",", "")

    print(f"Price: {price}")

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
