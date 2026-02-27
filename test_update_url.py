import requests
import getpass
payload =
{
    "data": {
        "type": "dois",
    "attributes": {
        "url": "https://example.org"
    }
  }
}

def test_update(doi):
    rest_api = "https://api.test.datacite.org/dois/" + doi
    user = "uzah"
    headers = 
    {
        "accept" : "application/vnd.api+json",
        "content-type": "application/json",
        "authorization": "Basic" + "encrypted_creds"
    }  
    response = requests.put(rest_api, json=payload, headers=headers)


    
    # Get password
    pwd = getpass.getpass(prompt="Enter MDS password (N.B.: you will *not* see any input as you type): ", stream=None)
    if not pwd:
        raise CancelledError()
