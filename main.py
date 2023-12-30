# Import necessary libraries
import requests
import pandas as pd

# URL of the JSON data
url = "https://s3.amazonaws.com/open-to-cors/assignment.json"

# Fetch the JSON data from the URL
response = requests.get(url)
data = response.json()

# Extract products data
products = data['products']

# Process and sort the data
# Convert products into a list of tuples (title, price, popularity)
product_list = [
    (details['title'], details['price'], details['popularity'])
    for _, details in products.items()
]

# Sort the products based on popularity (descending)
sorted_products = sorted(product_list, key=lambda x: x[2], reverse=True)

# Create a DataFrame for a tabular presentation
df = pd.DataFrame(sorted_products, columns=['Title', 'Price', 'Popularity'])

# Display the top 10 products
print(df.head(10))
