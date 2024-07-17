import json 
import boto3 
import os

def handler(event, context): 
    s3 = boto3.client("s3") 
    bucket = os.environ["BUCKET_NAME"] 

    records = event["Records"] 
    data = json.loads(records[0]["body"]) 
    categories = False
    if "categories" in data: 
        categories = True 
    if data["breeds"] == ["Unknown"]: 
        folder = "unknown_breed" 
    else: 
        folder = data["breeds"][0]["name"] 
    if categories: 
        folder += f"/{data['categories'][0]['name']}"
    s3.put_object(Bucket=bucket, Key=f"{folder}/{data['id']}.json", Body=json.dumps(data, indent=4)) 