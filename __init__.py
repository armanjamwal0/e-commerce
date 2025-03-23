import requests

# 'tv', 'audio', 'laptop', 'mobile', 'gaming', 'appliances
BASE_URL = "https://fakestoreapi.in/api/products"
URL = "https://fakestoreapi.in/api/products"

Url_category = "https://fakestoreapi.in/api/products/category"
response  = requests.get(BASE_URL)
data = response.json().get('products',[])
print(data) 


# for item in data:
#     print(item['gaming'])