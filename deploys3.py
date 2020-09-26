from s3 import S3


s3 = S3('s3','s3')
bucket_name = 's3demo.bkt.mm'
acl_permission = 'private'
region = 'ap-southeast-1'
bkt_response = s3.create_bucket(acl_permission,bucket_name,region)
print(bkt_response)

folder = ['css','fonts','images','js']
for i in folder:
    s3.create_folder(bucket_name,i)
print('Folders Created!')

s3.put_website(bucket_name)

s3.bucket_versioning(bucket_name)

