import requests
dois = 'dois.txt'
fh = open (dois, 'w')
url = "https://api.datacite.org/dois?prefix=10.15128&page[size]=1000&sort=name"

#get json data
headers = {"accept": "application/vnd.api+json"}
print('Getting JSON metadata from DataCite...')
response = requests.get(url, headers=headers)

#read json data
data = response.json()['data']
for rec in data:
    print(rec['id'] + "," + str(rec['attributes']['publicationYear']))
    fh.write(rec['id'] + "," + str(rec['attributes']['publicationYear']) + "\n")
