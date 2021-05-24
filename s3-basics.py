import boto3
import uuid
import time

s3_clinet = boto3.client('s3')
s3 = boto3.resource('s3')



def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])

test=create_bucket_name("s3-test")

def create_bucket(count):
    for i in range (count) :
        bucket_name= test + "python"  + str(i)
        create_response= s3_clinet.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration={
                                    'LocationConstraint': 'eu-west-1'})
        print (create_response)
        # time.sleep(10)

        s3.Bucket(bucket_name).upload_file("sample.py", "sample_"+ str(i) + ".py")

        # response = s3_clinet.delete_bucket(Bucket=bucket_name)
        # print (response)

# create_bucket(1)

list_bucket = s3_clinet.list_buckets()
print('Existing buckets:')
print (list_bucket)
for bucket in list_bucket['Buckets']:
    # print(f'  {bucket["Name"]}')
    b_name=(f'  {bucket["Name"]}').strip()
    if "s3-test" in b_name:
        print(b_name)
        copy_source = {
        'Bucket': b_name,
        'Key': 'sample.py'
        }

        bucket = s3.Bucket('easyaws.in')
        bucket.copy(copy_source, 'sample.py'+b_name.strip())




