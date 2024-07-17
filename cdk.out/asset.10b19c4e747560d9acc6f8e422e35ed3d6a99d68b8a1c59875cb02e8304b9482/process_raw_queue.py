import json 
import boto3
import os

def handler(event, context):  
    data = event 
    data1 = data["Records"][0]["body"]
    json_data = json.loads(data1) 
    output_record = [] 
    queue = boto3.client("sqs")   
    queue_url = os.environ["QUEUE_URL"]
    for cat in json_data: 
        if len(cat["breeds"]) == 0:
            cat["breeds"] = [{"name: unknown"}] 
        output_record.append(cat) 
        queue.send_message(QueueUrl=queue_url, MessageBody=json.dumps(output_record))


