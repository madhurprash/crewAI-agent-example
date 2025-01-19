Here is the Python code to upload a file to S3 using the specified model:

```python
import boto3
import sys

def upload_to_s3(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        return True
    except FileNotFoundError:
        print("The file was not found", file=sys.stderr)
        return False
    except NoCredentialsError:
        print("Credentials not available", file=sys.stderr)
        return False

def main():
    # Example usage
    file_name = 'path/to/your/file.txt'
    bucket_name = 'your-bucket-name'
    if upload_to_s3(file_name, bucket_name):
        print(f"{file_name} uploaded to {bucket_name}")
    else:
        print("Upload Failed", file=sys.stderr)

if __name__ == "__main__":
    main()
```

### Reasoning and Solution Steps:

1. **Initialize the S3 client**: Using `boto3.client('s3')` to create an S3 client object.
2. **Check if object_name is provided**: If not, use the filename as the object name in S3.
3. **Upload the file**: Using `s3_client.upload_file()` to upload the file.
4. **Handle exceptions**: Catch `FileNotFoundError` if the file does not exist and `NoCredentialsError` if AWS credentials are not available.
5. **Main function**: Define a `main()` function to demonstrate usage of the `upload_to_s3` function.
6. **Entry point**: Ensure the code runs as a standalone script by checking `if __name__ == "__main__":`.

This code provides a clear and functional way to upload a file to an S3 bucket using AWS SDK for Python (boto3).
