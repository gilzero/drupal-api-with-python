import requests
from requests.auth import HTTPBasicAuth

from pprint import pp

# Post Example
# https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module/creating-new-resources-post?utm_source=pocket_mylist


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
