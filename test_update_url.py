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
    user = "uzah"
    headers = {
        "accept" : "application/vnd.api+json",
        "content-type": "application/json",
#        "authorization": "Basic" + "encrypted_creds"
    }  
    # Get password
    pwd = getpass.getpass(prompt="Enter password for DataCite user (N.B.: you will *not* see any input as you type): ", stream=None)
#    print(pwd)
    basic = HTTPBasicAuth(user, pwd)
    payload['attributes']['url'] = url
    response = requests.put(rest_api, json=payload, headers=headers, auth=basic)
    print(response)

def main():
    try:
        test_update(sys.argv[1], sys.argv[2])
    except IndexError:
        print("Usage:\n", sys.argv[0], "DOI  URL")

if __name__ == "__main__":
    import sys
    sys.exit(main())
