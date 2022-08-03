import requests
import time

if __name__ == '__main__':
    data1 = []
    data2 = []

    headers = {'content-type': 'application/json', "Client-Id": "morteza", "Client-Password": "1234"}
    for i in range(100):
        data1.append({"lang": "fa",
                      "text": "آخرین مقام برجسته ژاپنی که پس از انقلاب 57 تاکنون به ایران سفر کرده است شینتارو آبه است."},
                     )
    for i in range(200):
        data2.append({"lang": "fa",
                      "text": "آخرین مقام برجسته ژاپنی که پس از انقلاب 57 تاکنون به ایران سفر کرده است شینتارو آبه است."},
                     )

    start_time = time.time()
    print(start_time)
    # for i in range(5):
    #     r1 = requests.post(url="http://127.0.0.1:8000/nerTest", json=data1, headers=headers)
    #     print(r1.json())
    print("--- %s seconds ---" % (time.time() - start_time))
    #     print(r1.json())
    for i in range(5):
        r1 = requests.post(url="http://127.0.0.1:8000/ner", json=data1, headers=headers)
        print(r1.json())
    for i in range(5):
        r1 = requests.post(url="http://127.0.0.1:8000/ner", json=data2, headers=headers)
        print(r1.json())
    # starttime = time.time()
    # headers = {'content-type': 'application/json', "Client-Id": "morteza", "Client-Password": "1234"}
    # while True:
    #     r2 = requests.get(url="http://127.0.0.1:8000/ner/10", headers=headers)
    #     time.sleep(5.0 - ((time.time() - starttime) % 5.0))
