import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Environment variables वरून सुरक्षितपणे Credentials घेणे
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = "sujata-cloud-project-2026"

def upload_file_to_s3(file_path):
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return

    file_name = os.path.basename(file_path)

    # S3 Client सुरुवात
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
    )

    try:
        print(f"Uploading '{file_name}' to AWS S3 bucket '{BUCKET_NAME}'...")
        s3_client.upload_file(file_path, BUCKET_NAME, file_name)
        print(f"Success! '{file_name}' uploaded successfully to AWS Cloud.")

    except NoCredentialsError:
        print("Error: AWS Credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS Credentials provided.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_file = "resume_test.txt"
    with open(test_file, "w") as f:
        f.write("AWS S3 File Upload Project completed successfully!")

    upload_file_to_s3(test_file)