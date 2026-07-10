import requests

def get_dois(prefix):
    coll = 'dois_resolve2collections.txt'
    fh1 = open(coll, 'w')
    rd = 'dois_resolve2researchdata.txt'
    fh2 = open(rd, 'w')
    other = 'dois_resolve_elsewhere.txt'
    fh3 = open(other, 'w')
    url = "https://api.datacite.org/dois?prefix=" + prefix + "&page[size]=1000&sort=name"

    #get json data
    headers = {"accept": "application/vnd.api+json"}
    print("Getting JSON metadata from DataCite...")
    response = requests.get(url, headers=headers)

    #read json data
    print("Reading JSON metadata...")
    rd_count = 0
    coll_count = 0
    other_count = 0
    data = response.json()['data']
    for rec in data:
        url = rec['attributes']['url']
        f = url.find('collections.durham.ac.uk')
        g = url.find('researchdata.durham.ac.uk')
        if f > 0:
            coll_count += 1
            print(rec['id'] + "," + str(rec['attributes']['publicationYear']))
            fh1.write(rec['id'] + "\n")
        if g > 0:
            rd_count += 1
            fh2.write(rec['id'] + "\n")            
        else:
            other_count += 1
#            print(rec['id'] + "," + str(rec['attributes']['publicationYear']) + "," + rec['attributes']['url'])
            fh3.write(rec['id'] + "," + rec['attributes']['url'] + "\n")
    print("Found {0} DOIs with prefix {1}".format(coll_count + rd_count + other_count, prefix))
    print("Created new file with " + str(coll_count) + " DOIs that resolve to collections: " + coll)
    print("Created new file with " + str(rd_count) + " DOIs that resolve to researchdata: " + rd)
    print("Created new file with " + str(other_count) + " DOIs that resolve elsewhere: " + other)


def main():
    try:
        get_dois(sys.argv[1])
    except IndexError:
        print("Usage:\n", sys.argv[0], "DOI_prefix")

if __name__ == "__main__":
    import sys
    sys.exit(main())
