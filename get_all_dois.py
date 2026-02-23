import requests

url = "https://api.datacite.org/dois?prefix=10.15128&fields[dois]=creators,titles&page[size]=10000&sort=name"

headers = {"accept": "text/csv"}

response = requests.get(url, headers=headers)

print(response.text)
