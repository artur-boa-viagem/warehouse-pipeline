import boto3
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

s3 = boto3.client('s3')

POKEMON_BUCKET = os.getenv('POKEMON_BUCKET')
def download_object(key, file_name):
    s3.download_file(POKEMON_BUCKET, key, file_name)

def get_object(key):
    try:
        response = s3.get_object(
            Bucket=POKEMON_BUCKET,
            Key=key,
        )
        if response == None or response["ResponseMetadata"]["HTTPStatusCode"] < 400:
            print("Objeto recebido com sucesso")
        else:
            print(f"Erro ao pegar objeto: {key}")

        return response["Body"]
    except Exception as e:
        print(f"Erro ao pegar objeto: {key}, exceção: {e}")
        raise e

def list_objects(prefix='', max_keys=1000):
    response = s3.list_objects_v2(Bucket=POKEMON_BUCKET, Prefix=prefix, MaxKeys=max_keys)
    
    if 'Contents' in response:
        return [obj['Key'] for obj in response['Contents']]
    else:
        return []
    
def upload_object(obj, key):
    try:
        response = s3.put_object(Bucket=POKEMON_BUCKET, Key=key, Body=obj)
        if response == None or response["ResponseMetadata"]["HTTPStatusCode"] > 400:
            print(f"Erro ao inserir objeto: {key}")
    except Exception as e:
        print(f"Erro ao inserir objeto: {key}, exceção: {e}")
        raise e
    
def create_folder(folder_name):
    try:
        response = s3.put_object(Bucket=POKEMON_BUCKET, Key=(folder_name + '/'))
        if response == None or response["ResponseMetadata"]["HTTPStatusCode"] > 400:
            print(f"Erro ao criar pasta: {folder_name}")
    except Exception as e:
        print(f"Erro ao criar pasta: {folder_name}, exceção: {e}")
        raise e
    
def delete_folder(folder_name):
    try:
        response = s3.delete_object(Bucket=POKEMON_BUCKET, Key=(folder_name + '/'))
        if response == None or response["ResponseMetadata"]["HTTPStatusCode"] > 400:
            print(f"Erro ao deletar pasta: {folder_name}")
    except Exception as e:
        print(f"Erro ao deletar pasta: {folder_name}, exceção: {e}")
        raise e
    
def list_folders(prefix=''):
    response = s3.list_objects_v2(Bucket=POKEMON_BUCKET, Prefix=prefix, Delimiter='/')
    
    if 'CommonPrefixes' in response:
        return [folder['Prefix'] for folder in response['CommonPrefixes']]
    else:
        return []
    
def list_objects_in_folder(folder_name):
    response = s3.list_objects_v2(Bucket=POKEMON_BUCKET, Prefix=folder_name, Delimiter='/')
    
    if 'Contents' in response:
        return [obj['Key'] for obj in response['Contents']]
    else:
        return []