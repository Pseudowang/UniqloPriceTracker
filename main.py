import requests
import json
from flask import Flask



url = "https://www.uniqlo.cn/data/products/spu/zh_CN/u0000000059115.json"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
} 

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    price_info ={
        "productId": data["rows"][0]["productId"],
        "productName": data["summary"]["name"],
        "originPrince": data["summary"]["originPrice"],
        "currentPrice": data["summary"]["maxVaryPrice"]
    }

else:
    print(f"Error: {response.status_code} - {response.text}")