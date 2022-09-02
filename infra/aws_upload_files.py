import boto3

s3 = boto3.client('s3')

path = "../input_data/ready/"
bucket_name = "s3-bucket-mrwatney"
data = ["products","customers","transactions"]

print("Uploading files")
for d in data:
    s3.upload_file(path+d+".csv", bucket_name, d+"/"+d+".csv")
    print("File "+d+".csv uploaded")
print("Uploading finished")