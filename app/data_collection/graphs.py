import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = '/home/tishok/Desktop/studies/Python/vmms_api/app/data_collection/ml.csv'
df = pd.read_csv(file_path)

# Graphs
# Companies with their sold Vehicles
plt.figure(figsize=(20, 5))
sns.countplot(x='manufacturer', data=df.sort_values(by='manufacturer'), hue='manufacturer', palette='husl',
              legend=False)
plt.grid(color="green", linestyle="--", linewidth=0.5)
plt.title("Companies with their sold Vehicles", fontdict={"family": "serif", "color": "blue", "size": 20})
plt.xticks(rotation=90)  # Optional: Rotate x labels for better visibility
plt.show()

# Districts with their sold Vehicles

sns.countplot(x='owner_district', data=df.sort_values(by='owner_district'), hue='owner_district', palette='husl',
              legend=False)
plt.grid(color="green", linestyle="--", linewidth=0.5)
plt.title("Districts with their sold Vehicles", fontdict={"family": "serif", "color": "blue", "size": 20})
plt.xticks(rotation=90)  # Optional: Rotate x labels for better visibility
plt.show()

plt.figure(figsize=(15, 4))
df.groupby('manufacturer')['purchase_price'].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90, legend=False)
plt.title("The income in different manufacturers", fontsize=20)
plt.show()
plt.figure(figsize=(20, 4))
earned_by_manufacturer = df.groupby('manufacturer')['purchase_price'].sum().sort_values(ascending=True).plot(
    kind='barh', color='g')
plt.title("Money earned from vehicle by manufacturer type", fontsize=20)
plt.xlabel("Manufacturer", fontsize=15)
plt.ylabel("Purchase Price", fontsize=15)
plt.xticks(rotation=45)  # Rotate x-tick labels for better visibility
plt.grid(color="green", linestyle="--", linewidth=0.5)
plt.show()

plt.figure(figsize=(20, 3))
# Create scatter plot for selling_price
sns.scatterplot(x='selling_price', y='purchase_price', data=df, color='r', label='Selling Price', alpha=0.6)
# Create scatter plot for purchase_price
sns.scatterplot(x='purchase_price', y='selling_price', data=df, color='b', label='Purchase Price', alpha=0.6)
plt.title("Scatter Plot between Selling Price and Purchase Price", fontsize=20)
plt.grid(color="green", linestyle="--", linewidth=0.5)
plt.xlabel("Price", fontsize=15)
plt.ylabel("Price", fontsize=15)
plt.legend()
plt.show()
plt.figure(figsize=(20, 3))
# Create the scatter plot for selling_price vs. purchase_price
sns.scatterplot(x='selling_price', y='purchase_price', data=df, color='b', alpha=0.6)
plt.title("Scatter Plot between Selling Price and Purchase Price", fontsize=20)
plt.grid(color="green", linestyle="--", linewidth=0.5)
plt.xlabel("Selling Price", fontsize=15)
plt.ylabel("Purchase Price", fontsize=15)
plt.show()

plt.figure(figsize = (20, 3))
numeric_columns = ['owner_age', 'selling_price', 'purchase_price', 'year', 'kilometers_driven']
heatmap_data = df[numeric_columns].corr()
sns.heatmap(heatmap_data, cmap = 'BuPu', annot = True)
plt.show()
