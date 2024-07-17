import json  
import urllib3 
import boto3 
from datetime import datetime

def handler(event, context):  
    http = urllib3.PoolManager()
    url = "https://api.thecatapi.com/v1/images/search?limit=10&api_key=live_04E0HWtzMnxDR5vA3dZWSMxa2v8mAbNyTUCfiRySKbFrBz30h2fqZAxHYb63fVju" 
    response = http.request('GET', url) 
    data = json.loads(response.data.decode('utf-8')) 
    file_contents = json.dumps(data, indent=4)   
    time = datetime.now()

    bucket_name = "730335431216-raw-bucket"
    s3 = boto3.client("s3")  
    s3.put_object(Bucket=bucket_name, Key=f"{time}-cat_data.json", Body=file_contents)
