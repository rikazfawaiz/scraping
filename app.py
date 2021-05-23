import requests
import pandas as pd

url = 'https://shopee.co.id/api/v4/search/search_items'

for page in range(1,101):
    param = {
        'by' : 'relevancy',
        'keyword' : 'senter',
        'limit' : 50,
        'newest' : 0,
        'order' : 'desc',
        'page_type' : 'search',
        'scenario' : 'PAGE_GLOBAL_SEARCH',
        'version' : 2,
        'page': page
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
    df.to_csv('products.csv',mode='a',index=False)
    # print(df)
    print('page :',page)









