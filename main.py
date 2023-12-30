
import requests
import pandas as pd

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"

response = requests.get(url)
data = response.json()

products = data['products']

product_list = [
    (details['title'], details['price'], details['popularity'])
    for _, details in products.items()
]
sorted_products = sorted(product_list, key=lambda x: x[2], reverse=True)

df = pd.DataFrame(sorted_products, columns=['Title', 'Price', 'Popularity'])

print(df.head(10))
