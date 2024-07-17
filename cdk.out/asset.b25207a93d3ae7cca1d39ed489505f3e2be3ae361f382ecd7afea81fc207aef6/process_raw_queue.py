import json 
import boto3
import os

def handler(event, context):  
    queue = boto3.client("sqs")   
    processed_url = os.environ["PROCESSED_URL"] 

    records = event["Records"]  
    data = json.loads(json.loads(records[0]["body"])) 
    for cat in data:  
        if len(cat["breeds"]) == 0: 
            cat["breeds"] = ["Unknown"] 
            folder = "unknown_breed" 
        else: 
            folder = cat["breeds"][0]["name"].lower().replace(" ", "_") 
        if "categories" in cat: 
            folder = f"unknown/{cat['categories'][0]['name'].lower().replace(' ', '_')}" 
            if len(cat["breeds"]) > 0: 
                folder = f"{cat['breeds'][0]['name'].lower().replace(' ', '_')}/{cat['categories'][0]['name'].lower().replace(' ', '_')}"
        queue.send_message(QueueUrl=processed_url, MessageBody=json.dumps(cat), folder_name=folder)
    


