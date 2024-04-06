import requests


url = "http://localhost:8000/m_user/"

x = requests.get(url=url)

for y in x.json():
    print(y)
print(x.request.headers)
print(x.request.body)
