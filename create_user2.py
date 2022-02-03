import requests
import json

mydata = open("data.json","r").read()
response = requests.post("https://reqres.in/api/users", data=json.loads(mydata))
print(response)
print(response.json())
print(response.headers['content-type'])
assert response.json()['job'] == 'developer'
