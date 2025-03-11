import boto3
import helpers

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

response = helpers.get_object('tutorial/currículo.jpg')
#print("reponse", response)

list = helpers.list_objects()
print("list", list)