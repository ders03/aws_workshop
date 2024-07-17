import json 
import boto3
import os

def handler(event, context):  
    queue = boto3.client("sqs")   
    raw_url = os.environ["RAW_URL"] 
    processed_url = os.environ["PROCESSED_URL"] 

    records = event["Records"]  
    data = json.loads(json.loads(records[0]["body"])) 
    for cat in data: 
        if len(cat["breeds"]) == 0: 
            cat["breeds"] = ["Unknown"] 
        queue.send_message(QueueUrl=processed_url, MessageBody=cat)
    


