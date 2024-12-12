import datetime

import pandas as pd
import requests

vehicles_url = "http://127.0.0.1:8000/api/v1/vehicles"
maintenance_url = "http://localhost:8000/maintenance"

vehicles_response = requests.get(vehicles_url)
maintenance_response = requests.get(maintenance_url)

vehicles_data = vehicles_response.json()
maintenance_data = maintenance_response.json()

df_vehicles = pd.DataFrame(vehicles_data)
df_maintenance_schedule = pd.DataFrame(maintenance_data)

df = pd.merge(df_vehicles, df_maintenance_schedule, left_on='id', right_on='vehicle_id', how='left')

df['vehicle_task'] = df['vehicle_name'] + " - " + df['task_name']

df['due_date'] = pd.to_datetime(df['due_date'], errors='coerce')
df['days_until_due'] = (df['due_date'] - pd.to_datetime(datetime.date.today())).dt.days

df['urgency'] = df['days_until_due'].apply(lambda x: 'Late' if x < 0 else 'On Time')

df['is_completed'] = df['completed'].apply(lambda x: 'Completed' if x == 1 else 'Pending')

print(df.head())

print(df.tail())

# df.to_csv('merged_data.csv', index=False)

df_concatenated = pd.concat([df_vehicles, df_maintenance_schedule], axis=1)

print(df_concatenated.head())
