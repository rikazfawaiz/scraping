import pandas as pd
from pandas.core.algorithms import duplicated

df = pd.read_csv('products.csv')
df = df['id_product']
print(df.count())
print(len(df.unique()))

# df = df.sort_values(ascending=True)

# f = open('id_products.txt','w')
# f.write(str(df))
# f.close()