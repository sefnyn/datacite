import requests

def get_dois(prefix):
    dois = 'dois_resolve2collections.txt'
    fh = open(dois, 'w')
    other = 'dois_resolve_elsewhere.txt'
    fh2 = open(other, 'w')
    url = "https://api.datacite.org/dois?prefix=" + prefix + "&page[size]=1000&sort=name"

    #get json data
    headers = {"accept": "application/vnd.api+json"}
    print("Getting JSON metadata from DataCite...")
    response = requests.get(url, headers=headers)

    #read json data
    print("Reading JSON metadata...")
    num = 0
    data = response.json()['data']
    for rec in data:
        num += 1
        url = rec['attributes']['url']
        f = url.find('collections.durham.ac.uk')
        if f > 0:
#            print(rec['id'] + "," + str(rec['attributes']['publicationYear']))
            fh.write(rec['id'] + "\n")
        else:
#            print(rec['id'] + "," + str(rec['attributes']['publicationYear']) + "," + rec['attributes']['url'])
            fh2.write(rec['id'] + "," + rec['attributes']['url'] + "\n")
    print("Created new file with DOIs that resolve to collections server: " + dois)
    print("Created new file with DOIs that resolve elsewhere: " + other)
    print("Found {0} DOIs with prefix {1}".format(num, prefix))

def main():
    try:
        get_dois(sys.argv[1])
    except IndexError:
        print("Usage:\n", sys.argv[0], "DOI_prefix")

if __name__ == "__main__":
    import sys
    sys.exit(main())
