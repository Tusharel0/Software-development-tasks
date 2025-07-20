import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set URL of the e-commerce search page
url = "https://www.flipkart.com/search?q=mobile"

# Set headers to mimic browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Lists to store data
product_names = []
prices = []
ratings = []

# Extract products
for item in soup.select("div._1AtVbE"):
    name = item.select_one("div._4rR01T")
    price = item.select_one("div._30jeq3")
    rating = item.select_one("div._3LWZlK")

    if name and price:
        product_names.append(name.text.strip())
        prices.append(price.text.strip())
        ratings.append(rating.text.strip() if rating else "No Rating")

# Store in DataFrame
df = pd.DataFrame({
    "Product Name": product_names,
    "Price": prices,
    "Rating": ratings
})

# Save to CSV
df.to_csv("flipkart_mobiles.csv", index=False)
print("Data saved to flipkart_mobiles.csv")
