import requests


url = "http://192.168.1.85:8000/"


def test_url(url=None) -> str:
    try:
        respons = requests.get(url=url)
    except:
        print("Connection refused by the server..")

    print(respons.status_code)
    print(respons.json())


test_url(url)
