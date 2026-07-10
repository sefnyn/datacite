import requests

def get_dois(prefix):
    dois = 'dois_resolve2sufia.txt'
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
    sufia_count = 0
    other_count = 0
    data = response.json()['data']
    for rec in data:
        url = rec['attributes']['url']
#        f = url.find('collections.durham.ac.uk')
        g = url.find('researchdata.durham.ac.uk')
#        if f > 0:
#            sufia_count += 1
#            print(rec['id'] + "," + str(rec['attributes']['publicationYear']))
#            fh.write(rec['id'] + "\n")
        if g > 0:
            sufia_count += 1
            fh.write(rec['id'] + "\n")            
        else:
            other_count += 1
#            print(rec['id'] + "," + str(rec['attributes']['publicationYear']) + "," + rec['attributes']['url'])
            fh2.write(rec['id'] + "," + rec['attributes']['url'] + "\n")
    print("Found {0} DOIs with prefix {1}".format(sufia_count + other_count, prefix))
    print("Created new file with " + str(sufia_count) + " DOIs that resolve to Sufia server: " + dois)
    print("Created new file with " + str(other_count) + " DOIs that resolve elsewhere: " + other)


def main():
    try:
        get_dois(sys.argv[1])
    except IndexError:
        print("Usage:\n", sys.argv[0], "DOI_prefix")

if __name__ == "__main__":
    import sys
    sys.exit(main())
