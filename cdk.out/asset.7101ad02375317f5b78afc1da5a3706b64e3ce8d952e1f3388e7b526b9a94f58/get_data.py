import json  
import urllib3 
import boto3 

def handler(event, context):  
    http = urllib3.PoolManager()
    url = "https://api.thecatapi.com/v1/images/search?limit=10&api_key=live_04E0HWtzMnxDR5vA3dZWSMxa2v8mAbNyTUCfiRySKbFrBz30h2fqZAxHYb63fVju" 
    response = http.request('GET', url) 
    data = json.loads(response.data.decode('utf-8'))  
    print(data) 
    print(response.status)
    
    bucket_name = "730335431216-raw-bucket"
    s3 = boto3.resource("s3")  
    s3.Bucket.put_object(Bucket=bucket_name, Key="cat_data.json", Body=json.dumps(data))
