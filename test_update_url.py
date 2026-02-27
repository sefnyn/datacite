import requests
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
        "content-type": "application/json"
    }  
    response = requests.put(rest_api, json=payload, headers=headers)


