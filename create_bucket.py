import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket = s3.create_bucket(
    Bucket='example-boto3-1235567qwerccse444',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    })
print (bucket)    
