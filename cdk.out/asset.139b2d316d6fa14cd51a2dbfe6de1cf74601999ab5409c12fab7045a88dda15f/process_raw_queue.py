import json 
import boto3
import os

def handler(event, context):  
    data = json.loads(event["Records"][0]["body"]) 
    output_record = [] 
    queue = boto3.client("sqs")   
    queue_url = os.environ["QUEUE_URL"]
    for cat in data: 
        if len(cat["breeds"]) == 0:
            cat["breeds"] = [{"name: unknown"}] 
        output_record.append(cat) 
        queue.send_message(queue_url, MessageBody=json.dumps(output_record))


