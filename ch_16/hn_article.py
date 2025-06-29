import requests
import json

#make an api call, nad store the responce

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"status code: {r.status_code}")

#explore the structures of the data
responce_dict = r.json()
responce_string = json.dumps(responce_dict,indent=4)
print(responce_string)