import boto3
import s3_service

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

response = s3_service.get_object('tutorial/currículo.jpg')
#print("reponse", response)

list = s3_service.list_objects()
print("list", list)