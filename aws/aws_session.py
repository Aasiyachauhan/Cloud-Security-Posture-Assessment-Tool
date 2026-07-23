import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def create_session():
    #Creates and returns an AWS session.
    try:
        session = boto3.Session()
        return session
    except Exception as error:
        print(f"[ERROR] Failed to create AWS session: {error}")
        return None