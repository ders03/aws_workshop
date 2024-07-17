import json 
import boto3
import os

def handler(event, context):  
    queue = boto3.client("sqs")   
    raw_url = os.environ["RAW_URL"] 
    processed_url = os.environ["PROCESSED_URL"] 

    records = event["Records"]
    print(type(records)) 
    print(next) 
    print(records)


