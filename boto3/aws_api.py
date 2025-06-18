import boto3

# Create the S3 client
s3_client = boto3.client('s3')

# List all buckets
response = s3_client.list_buckets()

def s3_bucket_list():
    bucket_list = []

    for bucket in response['Buckets']:
        print(bucket['Name'])
        bucket_list.append(bucket['Name'])

    print("\nAll buckets collected:", bucket_list)
    print()
    return bucket_list

# Call the function to get the bucket names
bucket_list = s3_bucket_list()

# Delete each bucket in the list 

###CAREFUL### this will delete your S3 buckets!!!

"""for bucket_name in bucket_list:
    try:
        print(f"Deleting bucket: {bucket_name}")
        s3_client.delete_bucket(Bucket=bucket_name)
    except Exception as e:
        print(f"Could not delete bucket {bucket_name}: {e}")"""

def deleteSingleBucket(buckt_name):
    deleter_response = s3_client.delete_bucket(
        Bucket = buckt_name
    )

# create bucket S3

"""def createBucket(bucket_name):
    creates3bucket = s3_client.create_bucket(
        Bucket= bucket_name
    )
    print(creates3bucket)

createBucket('madeupnametwobucket')"""


