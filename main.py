import time
import json
from Amazon import Amazon_Flipkart, Amazon_ProductDetails
from Flipkart import Flipkart_Amazon, Flipkart_ProductDetails

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Define the model for the input body
class URLRequest(BaseModel):
    url: str

@app.post("/process-url")
async def process_url(request: URLRequest):
    url = request.url
    is_success = False
    
    result = {
        "Flipkart": {},
        "Amazon": {}
    }

    if "flipkart" in url:
        flpkrt_title, flpkrt_price = Flipkart_ProductDetails(url)
        result["Flipkart"]["Title"] = flpkrt_title
        result["Flipkart"]["Price"] = flpkrt_price
        result["Flipkart"]["FlipkartLink"] = url

        amzn_redirect_link = Flipkart_Amazon(flpkrt_title)
        if amzn_redirect_link:
            amzn_title, amzn_price = Amazon_ProductDetails(amzn_redirect_link)
            result["Amazon"]["Title"] = amzn_title
            result["Amazon"]["Price"] = amzn_price
            result["Amazon"]["AmazonLink"] = amzn_redirect_link
            is_success = True
        else:
            result["Amazon"] = None
    else:
        amzn_title, amzn_price = Amazon_ProductDetails(url)
        result["Amazon"]["Title"] = amzn_title
        result["Amazon"]["Price"] = amzn_price
        result["Amazon"]["AmazonLink"] = url;

        flpkrt_redirect_link = Amazon_Flipkart(amzn_title)
        if flpkrt_redirect_link:
            flpkrt_title, flpkrt_price = Flipkart_ProductDetails(flpkrt_redirect_link)
            is_success = True
            result["Flipkart"]["Title"] = flpkrt_title
            result["Flipkart"]["Price"] = flpkrt_price
            result ["Flipkart"]["FlipkartLink"] = flpkrt_redirect_link
        else:
            result["Flipkart"] = None

    # Process the URL as needed
    if is_success:
        return {"message": "Success", "data": result}
    else:
        raise HTTPException(status_code=404, detail="Failed to process the URL")
