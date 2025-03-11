import boto3
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

s3 = boto3.client('s3')

BUCKET_NAME = os.getenv('BUCKET_NAME')
def download_object(key, file_name):
    s3.download_file(BUCKET_NAME, key, file_name)

def get_object(key):
    return s3.get_object(Bucket=BUCKET_NAME, Key=key)

def list_objects(prefix='', max_keys=1000):
    """
    Returns a list of object keys in the bucket with the given prefix.
    
    Args:
        prefix (str): Filter objects by prefix
        max_keys (int): Maximum number of keys to return
        
    Returns:
        list: List of object keys (strings)
    """
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix, MaxKeys=max_keys)
    
    if 'Contents' in response:
        return [obj['Key'] for obj in response['Contents']]
    else:
        return []