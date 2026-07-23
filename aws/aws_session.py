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

def verify_connection(session):
    #Verifies AWS credentials by checking the caller identity.
    try:
        sts = session.client("sts")
        identity = sts.get_caller_identity()
        print("[SUCCESS] AWS connection verified")
        print(f"Account ID: {identity['Account']}")
        print(f"User ARN: {identity['Arn']}")
        return True
    except NoCredentialsError:
        print("[ERROR] AWS credentials not found")
        return False
    except ClientError as error:
        print(f"[ERROR] AWS authentication failed: {error}")
        return False

