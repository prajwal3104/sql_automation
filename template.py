import os
from pathlib import Path
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s')


list_of_files = [
    ".github/workflows/.gitkeep",
    "src/cloud_functions/__init__.py",
    "src/cloud_functions/execute_sql_and_send_email.py",
    "src/cloud_functions/parse_and_insert_data.py",
    "src/sql_queries/query.sql",
    "src/main.py",
    "service_account_key.json",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent 


    if not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            f.write('')
        logging.info(f"Creating file: {filepath}")

    else:
        logging.info(f"{filepath} already exists")
