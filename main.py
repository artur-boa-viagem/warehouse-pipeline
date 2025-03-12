import boto3
import s3_service
from pokemon_pipeline.add_specific_pokemon_type import upload_specific_pokemon_type
from utils.pokemon_types import pokemon_types

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

def populate_pokemon_types():
    for type in pokemon_types:
        upload_specific_pokemon_type(type)

def create_folder(folder_name):
    s3_service.create_folder(folder_name)
    folders = s3_service.list_folders()
    print(folders)
    folters_inside = s3_service.list_folders(folder_name)
    print(folters_inside)

def delete_object(object_name):
    s3_service.delete_folder(object_name)
    folders = s3_service.list_folders()
    print(folders)

def upload_json(json, key):
    s3_service.upload_object(json,key)
    folders = s3_service.list_folders()
    print(folders)

# create_folder('teste2')
# upload_json('{"teste": "teste"}', 'teste/teste.json')
