import json 
import boto3
import os

def handler(event, context):  
    queue = boto3.client("sqs")   
    queue_url = os.environ["QUEUE_URL"] 
    response = queue.recieve_message(QueueUrl=queue_url
        WaitTimeSeconds=10,                                 
    ) 

    if 'Messages' in response: 
        message = response['Messages'][0] 
        message_body = message['Body'] 
        response_content = json.loads(message_body) 
    
        for cat in response_content: 
            if len(cat["breeds"]) == 0:
                cat["breeds"] = [{"name: unknown"}] 
            queue.send_message(QueueUrl=queue_url, MessageBody=json.dumps(cat))


