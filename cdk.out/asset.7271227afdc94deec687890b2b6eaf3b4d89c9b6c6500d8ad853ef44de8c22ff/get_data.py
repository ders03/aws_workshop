import requests as req 
import json 

def handler(event, context): 
    url = "https://api.thecatapi.com/v1/images/search?limit=10&api_key=live_04E0HWtzMnxDR5vA3dZWSMxa2v8mAbNyTUCfiRySKbFrBz30h2fqZAxHYb63fVju" 
    response = req.get(url) 
    data = response.json()  
    print(data)
    return data