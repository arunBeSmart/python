import boto3

s3_client = boto3.resource('s3')

for bucket in s3_client.buckets.all():

    print(bucket.name)
    