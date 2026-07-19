import logging
from google.cloud import storage

# 1. Configure professional logging instead of using 'print'
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def read_cloud_file(bucket_name, file_name):
    """
    Automates fetching and reading a file from a Google Cloud Storage bucket.
    """
    logging.info(f"Starting connection to GCP bucket: {bucket_name}")
    
    try:
        # 2. Connect to the Google Cloud Storage client
        storage_client = storage.Client()
        
        # 3. Get the specific bucket and file (blob)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        
        # 4. Download and decode the text content of the file
        logging.info(f"Attempting to download file: {file_name}")
        file_data = blob.download_as_text()
        
        logging.info("File successfully downloaded and processed!")
        return file_data

    except Exception as error:
        # 5. Catch errors (e.g., network down, bucket name wrong, file missing)
        logging.error(f"Failed to read file from cloud. Error details: {error}")
        return None

# This block allows you to test the script locally
if __name__ == "__main__":
    # We will replace these placeholder names with your actual GCP names next week
    TEST_BUCKET = "my-first-automation-bucket"
    TEST_FILE = "sample_data.txt"
    
    # Run the function
    content = read_cloud_file(TEST_BUCKET, TEST_FILE)
