import os
import pyodbc
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def execute_sql_and_send_email(request):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds, _ = google.auth.default()
            creds = creds.with_scopes(['https://www.googleapis.com/auth/gmail.modify'])

    conn_str = 'DRIVER={SQL Server};SERVER=<your_server>;DATABASE=<your_database>;UID=<your_username>;PWD=<your_password>'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    with open('../sql_queries/query.sql', 'r') as file:
        query = file.read()

    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        # Send Email
        gmail_service = build('gmail', 'v1', credentials=creds)
        message = create_message('<recipient_email>', '<sender_email>', 'Missing Data Required', 'Please fill in the missing data.')
        send_message(gmail_service, 'me', message)
        return 'Email sent successfully'
    else:
        return 'Query returned results'


def create_message(recipient, sender, subject, message_text):
    message = {
        'to': recipient,
        'from': sender,
        'subject': subject,
        'text': message_text
    }
    return message


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        return message
    except Exception as error:
        print('An error occurred:', error)
