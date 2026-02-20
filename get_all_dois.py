import requests

url = "https://api.test.datacite.org/dois"

headers = {"accept": "application/vnd.api+json"}

response = requests.get(url, headers=headers)

print(response.text)
