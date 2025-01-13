import time
import json
from Amazon import Amazon_Flipkart, Amazon_ProductDetails
from Flipkart import Flipkart_Amazon, Flipkart_ProductDetails

def main():
    url = input("Enter the URL of the product page: ")

    result = {
        "Flipkart": {},
        "Amazon": {}
    }

    if "flipkart" in url:
        flpkrt_title, flpkrt_price = Flipkart_ProductDetails(url)
        result["Flipkart"]["Title"] = flpkrt_title
        result["Flipkart"]["Price"] = flpkrt_price

        amzn_redirect_link = Flipkart_Amazon(flpkrt_title)
        if amzn_redirect_link:
            amzn_title, amzn_price = Amazon_ProductDetails(amzn_redirect_link)
            result["Amazon"]["Title"] = amzn_title
            result["Amazon"]["Price"] = amzn_price
        else:
            result["Amazon"] = None
    else:
        amzn_title, amzn_price = Amazon_ProductDetails(url)
        result["Amazon"]["Title"] = amzn_title
        result["Amazon"]["Price"] = amzn_price

        flpkrt_redirect_link = Amazon_Flipkart(amzn_title)
        if flpkrt_redirect_link:
            flpkrt_title, flpkrt_price = Flipkart_ProductDetails(flpkrt_redirect_link)
            result["Flipkart"]["Title"] = flpkrt_title
            result["Flipkart"]["Price"] = flpkrt_price
        else:
            result["Flipkart"] = None

    time.sleep(2)
    return json.dumps(result, indent=4)

if __name__ == "__main__":
    result_json = main()
    print(result_json)