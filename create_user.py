import requests


payload = {
        "name": "mukesh",
        "job": "automation"
        }

response = requests.post("https://reqres.in/api/users", data=payload)
print(response)
print(response.json())
assert response.json()['job'] == "automation" 
