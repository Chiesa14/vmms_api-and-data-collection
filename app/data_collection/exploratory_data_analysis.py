import requests
import pandas as pd

try:
    # Fetch ResearchProjects data
    research_projects_api = requests.get('http://127.0.0.1:8000/api/v1/vehicles')
    research_projects_api.raise_for_status()
    research_projects_api_data = research_projects_api.json()

    # Fetch Researchers data
    researchers_api = requests.get('http://localhost:8000/maintenance')
    researchers_api.raise_for_status()
    researchers_api_data = researchers_api.json()

    # Convert API responses to DataFrames
    rdf = pd.DataFrame(research_projects_api_data)
    researchers_df = pd.DataFrame(researchers_api_data)

    # Display DataFrames
    print("Vehicles Projects DataFrame:")
    print(rdf)
    print("\nMaintenance DataFrame:")
    print(researchers_df)

    # Perform an inner merge on the 'id' column
    inner_merged_df = pd.merge(rdf, researchers_df, on='id', how='inner')

    # Display merged DataFrame's shape and missing values count
    print("\nMerged DataFrame Shape:", inner_merged_df.shape)
    print("Missing Values in Merged DataFrame:")
    print(inner_merged_df.isnull().sum())

    # Fill missing values using forward fill method
    inner_merged_df.ffill(inplace=True)

    # Display the type of the DataFrame after filling missing values
    print("\nType of the DataFrame after forward fill:")
    print(type(inner_merged_df))

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")