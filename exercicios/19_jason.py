import json
import requests

# obj_json = json.dumps({"a": 1, "b": "Olá"}, ensure_ascii = False)
# print(obj_json)

# obj = json.loads('{"a": 1, "b": "Olá"}')
# print(obj['b'])

post = requests.post("http://httpbin.org/post", data = {"A": 1})
print(post.json()['headers'])