import requests
csv = 'dois.csv'
json = 'dois.json'
fh1 = open (csv, 'w')
fh2 = open (json, 'w')
url = "https://api.datacite.org/dois?prefix=10.15128&page[size]=1000&sort=name"

#get csv data
headers = {"accept": "text/csv"}
print('Getting CSV metadata from DataCite...')
response = requests.get(url, headers=headers)
print('Writing to file...')
fh1.write(response.text)

#get json data
headers = {"accept": "application/vnd.api+json"}
print('Getting JSON metadata from DataCite...')
response = requests.get(url, headers=headers)
print('Writing to file...')
fh2.write(response.text)



"""
print('Getting next page...')
print(response.meta)

next = response.links.next
response = requests.get(next, headers=headers)
fh = open (out, 'a')
fh.write(response.text)
"""
