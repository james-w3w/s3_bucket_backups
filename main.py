import boto3
import os

AWS_ACCESS_KEY_ID= os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

s3 = session.resource('s3')

def get_all_bucket_names():
    s3 = session.resource('s3')
    bucket_list = [bucket.name for bucket in s3.buckets.all()]
    print(len(bucket_list))
    return bucket_list

all_buckets = get_all_bucket_names()

def get_all_files_and_dirs(bucket_list):
    for item in bucket_list:
        your_bucket = s3.Bucket(item)
        print(your_bucket)

        for s3_object in your_bucket.objects.all():
                path, filename = os.path.split(s3_object.key)
                print(path, filename)
#
#            os.makedirs(path, exist_ok=True)
#            your_bucket.download_file(s3_object.key, f"{path}/{filename}")

get_all_files_and_dirs(all_buckets)