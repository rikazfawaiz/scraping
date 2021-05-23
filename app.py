import requests
import pandas as pd

url = 'https://shopee.co.id/api/v4/search/search_items'
param = {
    'by' : 'relevancy',
    'keyword' : 'celana',
    'limit' : 100,
    'newest' : 0,
    'order' : 'desc',
    'page_type' : 'search',
    'scenario' : 'PAGE_GLOBAL_SEARCH',
    'version' : 2,
    'page': 1
}

page = requests.get(url,params=param).json()
products = []
for item in page['items']:
    data = {
        'id_product' : item['item_basic']['itemid'],
        'name' : item['item_basic']['name'],
        'stock' : item['item_basic']['stock'],
        'price' : item['item_basic']['price']
    }
    products.append(data)

for x in products:
    print(x,end='\n')









