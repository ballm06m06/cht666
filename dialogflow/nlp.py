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
    
    try:
        result = json.loads(str(response.read(), encoding = "utf-8")) 
        print(result)
        return result
    except Exception as e:
        print(e)
    


    

    #return str(response.read(), encoding = "utf-8")