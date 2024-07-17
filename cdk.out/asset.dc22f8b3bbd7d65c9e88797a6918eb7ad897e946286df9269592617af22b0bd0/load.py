import json 
import boto3 
import os

def handler(event, context): 
    s3 = boto3.client("s3") 
    bucket = os.environ["BUCKET_NAME"] 

    records = event["Records"] 
    data = json.loads(json.loads(records[0]["body"])) 
    s3.put_object(Bucket=bucket, Key=f"{data['id']}.json", Body=json.dumps(data, indent=4)) 