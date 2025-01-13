import time
from Amazon import Amazon_Flipkart, Amazon_ProductDetails
from Flipkart import Flipkart_Amazon, Flipkart_ProductDetails

if __name__ == "__main__":
    url = input("Enter the URL of the product page: ")

    if url.__contains__("flipkart"):
        flpkrt_title,flpkrt_price = Flipkart_ProductDetails(url)    
        print(f"Flipkart Product Name ----> {flpkrt_title}\n")
        print(f"Flipkart Product Price ----> {flpkrt_price}\n")

        amzn_redirect_link = Flipkart_Amazon(flpkrt_title)
        if(amzn_redirect_link):
            print(f"Amazon Product Link -----> {amzn_redirect_link}\n")
            amzn_title,amzn_price = Amazon_ProductDetails(amzn_redirect_link)
            print(f"Amazon Product Name -----> {amzn_title}\n")
            print(f"Amazon Product Price -----> {amzn_price}\n")
        else:
            print("Product not found on Amazon.")
    else:
        amzn_title,amzn_price = Amazon_ProductDetails(url)
        print(f"Amazon Product Name -----> {amzn_title}\n")
        print(f"Amazon Product Price -----> {amzn_price}\n")

        flpkrt_redirect_link = Amazon_Flipkart(amzn_title)

        if(flpkrt_redirect_link):
            print(f"Flipkart Product Link -----> {flpkrt_redirect_link}\n")
            flpkrt_title,flpkrt_price = Flipkart_ProductDetails(flpkrt_redirect_link)
            print(f"Flipkart Product Name ----> {flpkrt_title}\n")
            print(f"Flipkart Product Price ----> {flpkrt_price}\n")
        else:
            print("Product not found on Flipkart.")
    time.sleep(2)




