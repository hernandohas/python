import requests

# # GET 
# resp = requests.get("https://github.com")
# print(resp.text)


# POST
resp = requests.post("http://httpbin.org/post")
print(resp.text)