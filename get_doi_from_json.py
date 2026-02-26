import requests
#json = 'dois.json'
#fh2 = open (json, 'w')
url = "https://api.datacite.org/dois?prefix=10.15128&page[size]=1000&sort=name"

#get json data
headers = {"accept": "application/vnd.api+json"}
print('Getting JSON metadata from DataCite...')
response = requests.get(url, headers=headers)

#read json data
data = response.json()['data']
for rec in data:
    print(rec['id'])
