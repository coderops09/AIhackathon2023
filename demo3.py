#creating a bucket in gcp
import os 
from google.cloud import storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\mande\python\pythonVenv\speech-to-text_demo\sa_speech_demo.json'
storage_client =storage.Client()

#create a new bucket
bucket_name='speech_text_demo_bucket'
bucket = storage_client.bucket(bucket_name)
bucket.location='US'
bucket = storage_client.create_bucket(bucket)

#print bucket
vars(bucket)

#access a specific bucket
my_bucket= storage_client.get_bucket('speech_text_demo_bucket')

#upload files
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket=storage_client.get_bucket(bucket_name)
        blob=bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False