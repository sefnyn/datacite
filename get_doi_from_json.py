import requests

def get_dois(prefix):
    dois = 'dois.txt'
    fh = open (dois, 'w')
    url = "https://api.datacite.org/dois?prefix=" + prefix + "&page[size]=1000&sort=name"

    #get json data
    headers = {"accept": "application/vnd.api+json"}
    print('Getting JSON metadata from DataCite...')
    response = requests.get(url, headers=headers)

    #read json data
    num = 0
    data = response.json()['data']
    for rec in data:
        num += 1
        url = rec['attributes']['url']
        f = url.find('collections.durham.ac.uk')
        if f > 0:
#            print(rec['id'] + "," + str(rec['attributes']['publicationYear']))
            fh.write(rec['id'] + "," + str(rec['attributes']['publicationYear']) + "\n")
        else:
#            print(rec['id'] + "," + str(rec['attributes']['publicationYear']) + "," + rec['attributes']['url'])
            fh.write(rec['id'] + "," + str(rec['attributes']['publicationYear']) + "," + rec['attributes']['url'] + "\n")
    print("Found {num} DOIs with prefix {prefix}")

def main():
    try:
        get_dois(sys.argv[1])
    except IndexError:
        print("Usage:\n", sys.argv[0], "DOI_prefix")

if __name__ == "__main__":
    import sys
    sys.exit(main())
