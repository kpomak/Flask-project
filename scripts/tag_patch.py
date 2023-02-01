import requests
from pprint import pprint

tag_id = 2
tag_name = "#django"

data = {
    "data": {
        "type": "tag",
        "attributes": {"name": tag_name, "id": tag_id},
        "id": tag_id,
        "relationships": {},
    }
}

headers = {"Accept": "application/json", "Content-type": "application/json"}

url = f"http://localhost:5000/api/tags/{tag_id}"

response = requests.patch(url, headers=headers, json=data)
pprint(response.json())
