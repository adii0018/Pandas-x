'''2. 📊 Exploratory Data Analysis (EDA) with Grouping'''
import pandas as pd

df = pd.read_csv("sales_data.csv")

# Total sales per region
region_sales = df.groupby('Region')['Sales'].sum()

# Average profit per category
category_profit = df.groupby('Category')['Profit'].mean()

# Top 5 products by revenue
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(5)

print(region_sales)
print(category_profit)
print(top_products)