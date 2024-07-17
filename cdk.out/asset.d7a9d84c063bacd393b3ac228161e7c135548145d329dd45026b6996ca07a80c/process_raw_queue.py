import json 
import boto3
import os

def handler(event, context):  
    records = event.get("Records", []) 
    if records: 
        data = records[0].get("body", "") 
        json_data = json.loads(data)  
        output_record = [] 
        queue = boto3.client("sqs")   
        queue_url = os.environ["QUEUE_URL"]
        for cat in json_data: 
            if len(cat["breeds"]) == 0:
                cat["breeds"] = [{"name: unknown"}] 
            output_record.append(cat) 
            queue.send_message(QueueUrl=queue_url, MessageBody=json.dumps(output_record))


