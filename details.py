import requests
import json


# Authentication data
auth_url = "http://20.244.56.144/test/auth"
auth_data ={'companyName': 'LENDI', 'clientID': '121137e9-2e2a-41de-a712-27b9e3a6b4e0', 'clientSecret': 'LfvOhmRKOYCueRTu', 'ownerName': 'Gottumukkala Sowmya', 'ownerEmail': '21kd1a1523@lendi.org', 'rollNo': '21KD1A1523'}
response = requests.post(auth_url, headers={"Content-Type": "application/json"}, data=json.dumps(auth_data))
auth_response = response.json()
print("Auth Response:", auth_response)

# Extract the token from the auth response
token = auth_response.get("token")

if token:
    # Use the token for an authenticated request to a protected endpoint
    api_url = "http://20.244.56.144/test/some-protected-endpoint"  # Replace with the actual API endpoint
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    api_response = requests.get(api_url, headers=headers)
    print("API Response:", api_response.json())
else:
    print("Failed to obtain the authorization token")