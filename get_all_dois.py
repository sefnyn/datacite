import requests

def get_dois(prefix):
    csv = 'dois.csv'
    json = 'dois.json'
    fh1 = open (csv, 'w')
    fh2 = open (json, 'w')
    url = "https://api.datacite.org/dois?prefix=" + prefix + "&page[size]=1000&sort=name"

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

def main():
    try:
        get_dois(sys.argv[1])
    except IndexError:
        print("Usage:\n", sys.argv[0], "DOI_prefix")

if __name__ == "__main__":
    import sys
    sys.exit(main())


