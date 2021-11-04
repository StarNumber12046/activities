import requests

print(requests.get("http://localhost:5555/get_status").content.decode())

print(requests.get("http://localhost:5555/return_important").content.decode())