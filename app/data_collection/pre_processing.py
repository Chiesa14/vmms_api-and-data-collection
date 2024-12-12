import pandas as pd
import requests
from sklearn.preprocessing import LabelEncoder

api_url = "http://localhost:8000"


def fetch_data(api_url, limit=2000000):
    response = requests.get(f"{api_url}/maintenance/", params={"limit": limit})
    if response.status_code == 200:
        try:
            data_res = response.json()
            return pd.DataFrame(data_res)
        except ValueError as e:
            raise Exception(f"Failed to parse JSON response: {e}")
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")


df = fetch_data(api_url)

df['due_date'] = pd.to_datetime(df['due_date'], errors='coerce')

label_encoder = LabelEncoder()
df['task_name'] = label_encoder.fit_transform(df['task_name'])

print(df.tail())
