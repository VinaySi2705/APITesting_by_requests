import requests

payload = {
    "name": "Vinay",
    "job": "testing"

}
response = requests.put("https://reqres.in/api/users/2", data=payload)
print(response)
print(response.json())
print(response.headers.get("Content-Type"))
assert response.json()['job'] == 'testing'
