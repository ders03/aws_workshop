import requests as req 
import json  
import urllib3

def handler(event, context):  
    http = urllib3.PoolManager()
    url = "https://api.thecatapi.com/v1/images/search?limit=10&api_key=live_04E0HWtzMnxDR5vA3dZWSMxa2v8mAbNyTUCfiRySKbFrBz30h2fqZAxHYb63fVju" 
    response = http.request('GET', url) 
    data = response.json()  
    print(data) 
    print(response.status)
    return data