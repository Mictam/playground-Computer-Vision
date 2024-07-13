import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../../../../data/exercises/dev_data_ops/sales_data.csv')

df['price'].fillna(df['price'].mean(), inplace=True)
df.dropna(subset=['sales', 'category'], inplace=True)

category_stats = df.groupby('category').agg({
    'sales': 'sum',
    'price': 'mean'
}).rename(columns={'sales': 'total_sales', 'price': 'average_price'}).reset_index()

print("\nCategory Statistics:")
print(category_stats)

df['price_category'] = np.where(df['price'] > 100, 'High Price', 'Low Price')

print("\nDataFrame with Price Category:")
print(df.head())

plt.figure(figsize=(10, 6))
plt.bar(category_stats['category'], category_stats['total_sales'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_sales_by_category.png')
plt.show()

df.to_csv('processed_products.csv', index=False)