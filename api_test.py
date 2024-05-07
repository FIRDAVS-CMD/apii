import json
from pprint import pp

import requests

url = "http://127.0.0.1:8000/api/v1/posts/"
put_url = "http://127.0.0.1:8000/api/v1/posts/3/"
payload = json.dumps({
    "title": "3 post",
    "content": "Uchinchiinchi content",
    "is_published": False
})

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic TGVub3ZvOjEyMzQ='
}


def get_all_posts():
    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    return json_data


def put():
    response = requests.request("PUT", put_url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    return json_data


if __name__ == "__main__":
    data = put()
    pp(data)
