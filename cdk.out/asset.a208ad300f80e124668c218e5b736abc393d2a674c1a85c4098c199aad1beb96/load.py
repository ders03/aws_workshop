import json 
import boto3 
import os

def handler(event, context): 
    s3 = boto3.client("s3") 
    sqs = boto3.client("sqs") 
    bucket = os.environ("BUCKET_NAME") 
    queue_url = os.environ("QUEUE_URL") 

    records = event["Records"] 
    data = json.loads(json.loads(records[0]["body"])) 
    s3.put_object(Bucket=bucket, Key=f"{data['id']}.json", Body=data)