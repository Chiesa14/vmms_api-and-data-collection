import datetime

import requests
import pandas as pd

api_url = "http://localhost:8000"

def fetch_data(api_url, limit=2000000):
    response = requests.get(f"{api_url}/maintenance/", params={"limit": limit})
    if response.status_code == 200:
        try:
            data = response.json()
            return pd.DataFrame(data)
        except ValueError as e:
            raise Exception(f"Failed to parse JSON response: {e}")
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

# Example usage
df = fetch_data(api_url)

print("**********************Summary**********************")
def describe_dataset(df):
    print("Dataset Summary:")
    print(df.info())
    print("\nSample Rows:")
    print(df.head())
    print("\nDataset Shape:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print("\nDataset Description (Numerical Columns):")
    print(df.describe())
    print("\nDataset Description (All Columns):")
    print(df.describe(include='all'))

describe_dataset(df)


print("\n\n\n**********************Null Value Handling**********************\n\n\n")


def find_null_values(df):
    print("Null Values Summary:")
    print(df.isnull().sum())
    print("\nPercentage of Null Values:")
    print((df.isnull().sum() / len(df)) * 100)

def replace_null_values(df):
    if 'due_date' in df.columns:
        df.fillna({'due_date': datetime.date.today()}, inplace=True)
    print(df.tail())


    return df

find_null_values(df)
replace_null_values(df)




