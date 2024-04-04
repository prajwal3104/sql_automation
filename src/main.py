from cloud_functions import execute_sql_and_send_email, parse_and_insert_data
from google.cloud import bigquery

# Set up Google Cloud client
BQ_PROJECT_ID = "onfinance-ai"
client = bigquery.Client(project=BQ_PROJECT_ID)

# Cloud Function 1 - Execute SQL & Send Email
def execute_sql(request):
    return execute_sql_and_send_email.execute_sql_and_send_email(request)

# Cloud Function 2 - Parse & Insert Data
def parse_email(request):
    return parse_and_insert_data.parse_and_insert_data(request)
