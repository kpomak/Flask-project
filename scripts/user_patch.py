import requests
from pprint import pprint

article_id = 1
headers = {"Accept": "application/json", "Content-type": "application/json"}
url = f"http://localhost:5000/api/users/{article_id}"

resp = requests.get(url).json()

response = requests.patch(url, headers=headers, json=resp).json()
pprint(response)
