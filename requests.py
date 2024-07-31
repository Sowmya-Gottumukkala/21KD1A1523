import requests
import json

# Registration
registration_url = "http://20.244.56.144/test/register"
registration_data = {
    "companyName": "LENDI",
  "ownerName": "Gottumukkala Sowmya",
  "rollNo": "21KD1A1523",
  "ownerEmail": "21kd1a1523@lendi.org",
  "accessCode":"BvLAwk"
}
response = requests.post(registration_url, headers={"Content-Type": "application/json"}, data=json.dumps(registration_data))
print(response.json())