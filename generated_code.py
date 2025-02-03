```python
# Import necessary modules from the AWS SDK
import boto3
from botocore.exceptions import NoCredentialsError

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket.

    :param file_name: File to upload
    :param bucket_name: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Initialize a session using Amazon S3
    s3_client = boto3.client('s3')

    try:
        # Upload the file
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded successfully to {bucket_name}/{object_name}")
        return True