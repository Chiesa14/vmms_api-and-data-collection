import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = '/home/tishok/Desktop/studies/Python/vmms_api/app/data_collection/ml.csv'
df = pd.read_csv(file_path)

print("***** Head *****")
print(df.head())
print("\n")

print("***** Describe *****")
print(df.describe())
print("\n")

print("***** Info *****")
print(df.info())
print("\n")

print("***** Shape *****")
print(df.shape)
print(f'Rows:{df.shape[0]}, Columns:{df.shape[1]} ')
print("\n")

print("***** Unique Values *****")
categorical_columns = df.select_dtypes(include=["object"]).columns
for col in categorical_columns:
    unique_values = df[col].unique()
    print(f"{col}: {len(unique_values)} unique values")
print("\n")

print("***** Value counts *****")
for col in df.columns:
    print(f'{df[col].value_counts()}')
print("\n")

print("***** Column names *****")
print(f'{df.columns.tolist()}')
print("\n")

print("***** Data types *****")
print(f'{df.dtypes}')
print("\n")

print("***** Data CLeaning *****")
# removing unwanted data in dataset
deleted_cols = df
deleted_cols.drop(['owner_name', 'vin'], axis=1, inplace=True)
# checking null values
print(deleted_cols.isnull().sum())
# Forward fill
deleted_cols.ffill()
# Backward fill
deleted_cols.backfill()
print(deleted_cols.isnull().sum())
print("\n")

print("***** Changing Datatypes *****")

"""errors parameter can contain {
raise: (default) raises an error for invalid parsing.
coerce: converts invalid parsing to NaN
ignore: returns the original data without any changes
} """
df['selling_price'] = df['selling_price'].astype(float)
df["purchase_price"] = pd.to_numeric(df["purchase_price"], errors="coerce", downcast="float")
df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")
print(df.dtypes)


print("***** Aggregated Statistics *****")

grouped_data = df.groupby('manufacturer').agg({
    'seating_capacity': ['min', 'max', 'mean', 'std', 'first', 'last'],
    'selling_price': ['min', 'max', 'mean', 'std', 'sum'],
    'purchase_price': ['min', 'max', 'mean', 'std', 'sum']
})

print(grouped_data)

print("***** Correlation *****")

print('Correlation between selling_price and kilometers_driven:', df['selling_price'].corr(df['kilometers_driven']))

print("***** Remove outliers *****")
# Remove outliers from the original DataFrame
inner_merged_df = df[df['selling_price'] > 1500]
print(inner_merged_df.head())