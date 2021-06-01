import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name="example-boto3-1235567qwerccse444"

fileupload= s3.Bucket(bucket_name).upload_file('README.md', 'README.md')

s3.Object(bucket_name,'README.md').delete()
