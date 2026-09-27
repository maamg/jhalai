from google.cloud import bigquery

-- # Create a Client object
client = bigquery.Client()

-- Creating a reference of dataset
dataset_ref = client.dataset('')