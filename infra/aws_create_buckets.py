import boto3

s3 = boto3.client('s3')

bucket_name = "s3-bucket-mrwatney"
directories = ["products","customers","transactions"]

print("Creating S3 objects started")

print("Creating bucket "+bucket_name)
s3.create_bucket(Bucket=bucket_name)
print("Bucket "+bucket_name+" created")

for directory in directories:
    s3.put_object(Bucket=bucket_name, Key=(directory+'/'))
    print("Created folder: "+directory)
    
print("Creating S3 objects finished")