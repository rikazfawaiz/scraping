# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

import requests
import pandas as pd

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
# header = {'User-Agent':user_agent,}

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









