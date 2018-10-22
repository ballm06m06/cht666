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
        print('intent nlp exception: '+ str(e))

def get_district(msg):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'zh-TW'
    request.query = msg
    response = request.getresponse()
    
    try:
        result = json.loads(str(response.read(), encoding = "utf-8")) 
        print(result)
        
        #找不到意圖 
        if result['result']['parameters'] == {}:
            
            return 'none'
        
        elif result['result']['parameters']['get_district'] == '臺北市':

            return 0

        elif result['result']['parameters']['get_district'] == '新北市':
            
            return 1

        elif result['result']['parameters']['get_district'] == '桃園市':
            
            return 2

        elif result['result']['parameters']['get_district'] == '臺中市':
            
            return 3

        elif result['result']['parameters']['get_district'] == '臺南市':
            
            return 4

        elif result['result']['parameters']['get_district'] == '高雄市':

            return 5

        elif result['result']['parameters']['get_district'] == '基隆市':
            
            return 6

        elif result['result']['parameters']['get_district'] == '新竹縣':
            
            return 7

        elif result['result']['parameters']['get_district'] == '新竹市':
            
            return 8

        elif result['result']['parameters']['get_district'] == '苗栗縣':
            
            return 9

        elif result['result']['parameters']['get_district'] == '彰化縣':

            return 10

        elif result['result']['parameters']['get_district'] == '南投縣':
            
            return 11

        elif result['result']['parameters']['get_district'] == '雲林縣':
            
            return 12

        elif result['result']['parameters']['get_district'] == '嘉義縣':
            
            return 13

        elif result['result']['parameters']['get_district'] == '嘉義市':
            
            return 14

        elif result['result']['parameters']['get_district'] == '屏東縣':

            return 15

        elif result['result']['parameters']['get_district'] == '宜蘭縣':
            
            return 16

        elif result['result']['parameters']['get_district'] == '花蓮縣':
            
            return 17

        elif result['result']['parameters']['get_district'] == '臺東縣':
            
            return 18

        elif result['result']['parameters']['get_district'] == '澎湖縣':
            
            return 19

        elif result['result']['parameters']['get_district'] == '金門縣':
            
            return 20

        elif result['result']['parameters']['get_district'] == '連江縣':
            
            return 21
        
        #not found
        else
            
            return 'none'

    except Exception as e:
        print('intent nlp exception: '+ str(e))
