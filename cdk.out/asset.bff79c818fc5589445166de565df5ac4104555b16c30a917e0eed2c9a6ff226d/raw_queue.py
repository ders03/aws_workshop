import boto3
import json 
import urllib.parse

def handler(event, context): 
    sqs = boto3.client("sqs") 
    s3 = boto3.client("s3")
    queue_url = "url here" 

    bucket = event["Records"][0]["s3"]["bucket"]["name"] 
    key = urllib.parse.unquote_plus(event["Records"][0]["s3"]["object"]["key"], encoding="utf-8") 
    response = s3.get_object(Bucket=bucket, Key=key) 
    sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(response["Body"].read().decode("utf-8")))