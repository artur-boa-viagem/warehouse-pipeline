import boto3
import s3_service
from pokemon_pipeline.add_specific_pokemon_type import upload_specific_pokemon_type
from utils.pokemon_types import pokemon_types

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

list = s3_service.list_objects()
print("list", list)

#populate s3 with pokemon divided by type
for type in pokemon_types:
    upload_specific_pokemon_type(type)