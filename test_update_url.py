import requests
from requests.auth import HTTPBasicAuth
import getpass
payload = {
    "data": {
        "type": "dois",
        "attributes": {
            "url": "https://example.org"
    }
  }
}

def test_update(doi, url):
    rest_api = "https://api.test.datacite.org/dois/" + doi
    user = "bl.durham"
    headers = {
        "accept" : "application/vnd.api+json",
        "content-type": "application/json",
    }  
    # Get password
    pwd = getpass.getpass(prompt="Enter password for DataCite user (N.B.: you will *not* see any input as you type): ", stream=None)
    basic = HTTPBasicAuth(user, pwd)
    payload['data']['attributes']['url'] = url
    response = requests.put(rest_api, json=payload, headers=headers, auth=basic)
    print(response.text)

def main():
    try:
        test_update(sys.argv[1], sys.argv[2])
    except IndexError:
        print("Usage:\n", sys.argv[0], "SHORT_DOI  URL")

if __name__ == "__main__":
    import sys
    sys.exit(main())




"""
import requests

url = "https://api.test.datacite.org/dois/10.4124%2FR90R967372K"

payload = { "data": {
        "type": "dois",
        "attributes": {
            "doi": "10.5438/0014",
            "prefix": "10.5438",
            "suffix": "0014",
            "identifiers": [
                {
                    "identifier": "https://doi.org/10.5438/0014",
                    "identifierType": "DOI"
                }
            ],
            "creators": [{ "name": "DataCite Metadata Working Group" }],
            "titles": [{ "title": "DataCite Metadata Schema Documentation for the Publication and Citation of Research Data v4.1" }],
            "publisher": "DataCite",
            "publicationYear": 2017,
            "types": { "resourceTypeGeneral": "Text" },
            "url": "https://schema.datacite.org/meta/kernel-4.1/"
        }
    } }
headers = {
    "accept": "application/vnd.api+json",
    "content-type": "application/json",
    "authorization": "Basic dXphaDpXYWQrUmFtcm9kPWhhbmdvdmVy"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)

"""
