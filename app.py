import requests
import pandas as pd

url = 'https://shopee.co.id/api/v4/search/search_items'

param = {
    'by' : 'relevancy',
    'keyword' : 'senter',
    'limit' : 50,
    'newest' : 0,
    'order' : 'desc',
    'page_type' : 'search',
    'scenario' : 'PAGE_GLOBAL_SEARCH',
    'version' : 2,
    'page': 0
}

items = requests.get(url,params=param).json()
products = []
for item in items['items']:
    data = {
        'id_product' : item['item_basic']['itemid'],
        'name' : item['item_basic']['name'],
        'stock' : item['item_basic']['stock'],
        'price' : item['item_basic']['price']
    }
    products.append(data)

df = pd.DataFrame.from_dict(products)
df.to_csv('products.csv',mode='w',index=False)

print(len(df['id_product'].unique()))










