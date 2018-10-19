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
        
        #找不到意圖 >> OLAMI
        if result['result']['parameters'] == {}:
            
            return 'none'
        #水質資訊
        elif result['result']['parameters']['get_Water_Info'][0] == '水質資訊':

            return '水質資訊'
        #溫度
        elif result['result']['parameters']['get_Water_Info'][0] == '溫度':

            return '溫度'
        #酸鹼度
        elif result['result']['parameters']['get_Water_Info'][0] == '酸鹼度':

            return '酸鹼度'
        #溶氧量
        elif result['result']['parameters']['get_Water_Info'][0] == '溶氧量':

            return '溶氧量'

            
    except Exception as e:
        print('nlp exception: '+ str(e))
