import requests
from requests.auth import HTTPBasicAuth
import json

# 1. DOUBLE CHECK THIS URL (Must have /rest/api/3/issue)
url = "https://mrazahofficial.atlassian.net/rest/api/3/issue"

# 2. ARE YOU SURE THE TOKEN IS FRESH? 
# Create a new one here: https://id.atlassian.com/manage-profile/security/api-tokens
email = "abc@gmail.com"
token = ""

auth = HTTPBasicAuth(email, token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

# Simplified payload to rule out other errors
payload = json.dumps({
    "fields": {
        "project": {
            "key": "KAN"
        },
        "summary": "Testing from Python",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "text": "Sent from GitHub Codespaces",
                            "type": "text"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "id": "10045"
        }
    }
})

response = requests.request("POST", url, data=payload, headers=headers, auth=auth)

if response.status_code == 201:
    print("Success! Issue Created.")
    print(response.text)
else:
    print(f"Failed with status: {response.status_code}")
    print(response.text)
