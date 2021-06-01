import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

list_bucket=client.list_buckets()

for bucket in list_bucket['Buckets']:
    print(bucket['Name'])
