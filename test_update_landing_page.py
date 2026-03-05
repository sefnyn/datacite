"""
Usage:
 test_update_landing_page.py [SHORT_DOI] [LANDING_PAGE]
"""

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

def test_update(pwd, doi, url):
    user = "bl.durham"
    basic = HTTPBasicAuth(user, pwd)
    rest_api = "https://api.test.datacite.org/dois/" + doi
    headers = {
        "accept" : "application/vnd.api+json",
        "content-type": "application/json",
    }  
    payload['data']['attributes']['url'] = url
    response = requests.put(rest_api, json=payload, headers=headers, auth=basic)
    try:
        d = response.json()['data']
        print("Success.  Updated landing page for DOI " + doi)
    except KeyError:
        e = response.json()['errors']
        print(response.text)
        print("Did not update DOI " + doi)

def main():
    # Get password
    pwd = getpass.getpass(prompt="Enter password for DataCite user (N.B.: you will *not* see any input as you type): ", stream=None)
    try:
        test_update(pwd, sys.argv[1], sys.argv[2])
    except IndexError:
        print("Usage:\n", sys.argv[0], "[SHORT_DOI] [LANDING_PAGE]")

if __name__ == "__main__":
    import sys
    sys.exit(main())
