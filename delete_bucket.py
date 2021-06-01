import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name="example-boto3-1235567qwerccse444"

response = client.delete_bucket(
    Bucket=bucket_name,
)

print(response)
