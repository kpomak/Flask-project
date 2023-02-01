import requests
from pprint import pprint

article_id = 1
headers = {"Accept": "application/json", "Content-type": "application/json"}
url = f"http://localhost:5000/api/users/{article_id}"

resp = requests.get(url).json()
print("users wAS GOT")

"""
{'data': {'attributes': {'body': 'The same language',
                         'dt_created': '2023-01-24T08:21:15.577421',
                         'dt_updated': '2023-01-24T08:21:15.601430',
                         'title': 'Pyhton'},
          'id': '1',
          'links': {'self': 'article_detail'},
          'relationships': {'author': {'links': {'related': 'author_detail'}},
                            'tags': {'links': {'related': 'tag_detail'}}},
          'type': 'article'},
"""

response = requests.patch(url, headers=headers, json=resp).json()
pprint(response)
