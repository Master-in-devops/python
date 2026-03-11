import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

try:
    # 1. Fetch the data from AWS
    response = s3.list_buckets()

    # 2. Extract the list of bucket dictionarie
    print("--- S3 Buckets (Client) ---")
    for bucket in response['Buckets']:
        print(f"Bucket Name: {bucket['Name']}")

except Exception as e:
    print(f"Failed to list buckets: {e}")