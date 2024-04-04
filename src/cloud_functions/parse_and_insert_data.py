import base64
import re
import pyodbc
from google.oauth2 import service_account
from googleapiclient.discovery import build

def parse_and_insert_data(request):
    request_json = request.get_json()
    email_data = base64.urlsafe_b64decode(request_json['message']['data']).decode('utf-8')

    extracted_data = re.findall(r'(\d+)', email_data)

    conn_str = 'DRIVER={SQL Server};SERVER=<your_server>;DATABASE=<your_database>;UID=<your_username>;PWD=<your_password>'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO <table_name> VALUES (?, ?)", extracted_data)
    conn.commit()
    conn.close()

    return 'Data inserted successfully'
