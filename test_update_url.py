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
    try:
        d = response.json()['data']
        print(response.text)
    except KeyError:
        e = response.json()['errors']
        print(response.text)
#        print('An error occurred while updating the landing page')
#        print(e['status'])
#        print(e['title'])

def main():
    try:
        test_update(sys.argv[1], sys.argv[2])
    except IndexError:
        print("Usage:\n", sys.argv[0], "SHORT_DOI  URL")

if __name__ == "__main__":
    import sys
    sys.exit(main())
