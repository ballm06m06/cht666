import requests
import json

my_headers = {'CK': 'PK0A8SOEKLX09I99YV'}

def get_ph_value():
    r = requests.get('https://iot.cht.com.tw/iot/v1/device/4514164539/sensor/PH/rawdata', headers = my_headers)
    if r.status_code == requests.codes.ok:
        print(r.text)
        jsonData = json.loads(r.text)
        print (jsonData['value'][0])

        return jsonData['value'][0]

def get_do_value():
    r = requests.get('https://iot.cht.com.tw/iot/v1/device/4514164539/sensor/DO/rawdata', headers = my_headers)
    if r.status_code == requests.codes.ok:
        print(r.text)
        jsonData = json.loads(r.text)
        print (jsonData['value'][0])

        return jsonData['value'][0]

def get_tmp_value():
    r = requests.get('https://iot.cht.com.tw/iot/v1/device/4514164539/sensor/TMP/rawdata', headers = my_headers)
    if r.status_code == requests.codes.ok:
        print(r.text)
        jsonData = json.loads(r.text)
        print (jsonData['value'][0])

        return jsonData['value'][0]