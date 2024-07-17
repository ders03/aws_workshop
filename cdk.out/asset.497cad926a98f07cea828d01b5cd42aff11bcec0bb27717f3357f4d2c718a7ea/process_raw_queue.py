import json 
import boto3
import os

def handler(event, context):  
    queue = boto3.client("sqs")   
    raw_url = os.environ["RAW_URL"] 
    processed_url = os.environ["PROCESSED_URL"] 
    response = queue.receive_message(QueueUrl=raw_url, 
        WaitTimeSeconds=1,                                 
    ) 

    if 'Messages' in response: 
        message = response['Messages'][0] 
        message_body = message['Body'] 
        response_content = json.loads(message_body) 
    
        for cat in response_content: 
            if len(cat["breeds"]) == 0:
                cat["breeds"] = [{"name: unknown"}] 
            queue.send_message(QueueUrl=processed_url, MessageBody=json.dumps(cat))


