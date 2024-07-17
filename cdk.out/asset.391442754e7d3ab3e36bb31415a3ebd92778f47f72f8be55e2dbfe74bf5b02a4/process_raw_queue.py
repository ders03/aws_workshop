import json 

def handler(event, context):  
    for record in event["Records"]: 
        print(record["body"])
    print(json.dumps(event)) 
    return {
        "statusCode": 200, 
        "body": json.dumps(event), 
    }