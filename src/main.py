from cloud_functions import execute_sql_and_send_email, parse_and_insert_data
from google.cloud import bigquery

BQ_PROJECT_ID = "onfinance-ai"
client = bigquery.Client(project=BQ_PROJECT_ID)

def execute_sql(request):
    return execute_sql_and_send_email.execute_sql_and_send_email(request, BQ_PROJECT_ID)

def parse_email(request):
    return parse_and_insert_data.parse_and_insert_data(request)

# Example usage:
if __name__ == "__main__":
    sample_request = {}  # Provide sample request if needed
    print(execute_sql(sample_request))
