import requests

# Below we get Response object called re,
#we can get all the information we need from this object
re = requests.get("https://reqres.in/api/users?page=2")

code = re.status_code
assert code == 200 ,"Code doesn't match"

# Through response.text we will get the data in string format
#print("Text",re.text)

# Through response.json() we will get the data in json format
print("Json",re.json())
print(type(re.headers))
print("headers",re.headers)
print(re.cookies)
print(re.encoding)
print(re.url)
