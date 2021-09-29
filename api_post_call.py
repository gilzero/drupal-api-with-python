import requests
from requests.auth import HTTPBasicAuth

from pprint import pp

"""
Example to call Drupal 9 API with POST method to create new content.
Related explaination post is at 
https://weimingchenzero.medium.com/use-python-to-call-drupal-9-core-restful-api-to-create-new-content-9f3fa8628ab4
"""

endpoint = 'https://drupal9.site/jsonapi/node/article'

u = 'username'
p = 'password'

headers = {
    'Accept': 'application/vnd.api+json',
    'Content-Type': 'application/vnd.api+json'
}

payload = {
    "data": {
        "type": "node--article",
        "attributes": {
            "title": "What's up from Python",
            "body": {
                "value": "Be water. My friends.",
                "format": "plain_text"
            }
        }
    }
}

r = requests.post(endpoint, headers=headers, auth=(u, p), json=payload)

# pp(r.headers)
# pp(r.status_code)
# pp(r.json())
