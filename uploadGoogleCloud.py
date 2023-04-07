import os
from google.cloud import storage
import datetime

def uploadtocloud():
    current_time = datetime.datetime.now()
    # Set the path of the service account key file
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'fluent-flame-382905-2daf37946219.json'
    # Initialize Google Cloud Storage client
    client = storage.Client()
    # Get bucket reference
    bucket = client.bucket('alzheimer-detection')
    # Set the path of the local file to upload
    local_file_path = 'medical_report.pdf'
    # Set the name of the file in the bucket
    remote_file_name = f'reports/report{current_time}.pdf'
    # Upload file to the bucket
    blob = bucket.blob(remote_file_name)
    blob.upload_from_filename(local_file_path)
    print(f'File {local_file_path} uploaded to bucket {bucket.name} in folder reports with name {remote_file_name}')
