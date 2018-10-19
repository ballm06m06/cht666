#!/usr/bin/python
#coding:utf-8
import apiai
import json
from cht_package.config import CLIENT_ACCESS_TOKEN


def get_intent(msg):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'zh-TW'
    request.query = msg
    response = request.getresponse()
    
    print(str(response, encoding = "utf-8"))
    print(str(response.read(), encoding = "utf-8"))

    return str(response.read(), encoding = "utf-8")