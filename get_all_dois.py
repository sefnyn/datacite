import requests
out = 'dois.csv'
fh = open (out, 'w')

url = "https://api.datacite.org/dois?prefix=10.15128&fields[dois]=creators,titles&page[size]=10000&sort=name"

headers = {"accept": "text/csv"}

response = requests.get(url, headers=headers)

print('Writing to file')
fh.write(str(response))
