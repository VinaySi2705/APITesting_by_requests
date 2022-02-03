import requests


# To auth we assigned username and password in tuple
response = requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('admin','admin'))
print(response.status_code)
