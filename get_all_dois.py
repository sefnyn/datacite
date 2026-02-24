import requests
out = 'dois.csv'
fh = open (out, 'w')

url = "https://api.datacite.org/dois?prefix=10.15128&page[size]=1000"
headers = {"accept": "text/csv"}

print('Getting metadata from DataCite...')
response = requests.get(url, headers=headers)

print('Writing to file...')
fh.write(response.text)

print('Getting next page...')
next = "https://api.datacite.org/dois?page[number]=1&page[size]=1000&prefix=10.15128:x"
response = requests.get(next, headers=headers)
fh = open (out, 'a')
fh.write(response.text)
