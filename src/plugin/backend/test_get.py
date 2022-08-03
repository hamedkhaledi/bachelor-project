import requests
import time

if __name__ == '__main__':
    headers = {'content-type': 'application/json', "Client-Id": "morteza", "Client-Password": "1234"}
    r2 = requests.get(url="http://127.0.0.1:8000/ner/1", headers=headers)
    print(r2.json())
    print(time.time())
