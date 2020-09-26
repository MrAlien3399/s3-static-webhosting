import boto3


class S3:
    def __init__(self, client,resource):
        self.client = boto3.client(client)
        self.resource = boto3.resource(resource)
        """ :type : pyboto3.s3 """

    def create_bucket(self,permission,bkt,bkt_region):
        print('Creating bucket')
        try:
            return self.client.create_bucket(
                ACL=permission,
                Bucket=bkt,
                CreateBucketConfiguration={
                    'LocationConstraint': bkt_region
                }
            )
        except:
            return f"Bucket {bkt} already exists or bucket name not globally unique!"
    
    def create_folder(self,bkt,dir_name):
        print(f'Creating {dir_name} folder')
        return self.client.put_object(Bucket = bkt,Key = (dir_name + '/'))

    def put_website(self,bkt):
        return self.client.put_bucket_website(
             Bucket = bkt,
             WebsiteConfiguration = {
                 'ErrorDocument' : {
                     'Key' : 'error.html',
                 },
                 'IndexDocument' : {
                     'Suffix' : 'index.html',
                 }
             }
         )

    def bucket_versioning(self,bkt):
        return self.client.put_bucket_versioning(
            Bucket = bkt,
            VersioningConfiguration = {
                'MFADelete' : 'Enabled',
                'Status' : 'Enabled'
            }
        )
