import requests
import json



def get_userFishType(id):
    my_data = {'id': 'U4'} 

    r = requests.post('https://cht666-node.herokuapp.com/fishowner/id', data = my_data)



    if r.status_code == requests.codes.ok:
        #print (r.text)
        jsonData = json.loads(r.text)
        #print(len(jsonData['response']))
        #print(jsonData['response'][0]['fishtype'])
        mlist = jsonData['response'][0]['fishtype'].split(',')
        
        try:
            mlist = []
            mlist = jsonData['response'][0]['fishtype'].split(',')
            
            return mlist
        except Exception as e:
            print('get user fish type exception:'+str(e))
            return []
        