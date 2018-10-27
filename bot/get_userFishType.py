import requests
import json



def get_userFishType(id):
    my_data = {'id': id} 

    r = requests.post('https://cht666-node.herokuapp.com/fishowner/id', data = my_data)

    if r.status_code == requests.codes.ok:
        #print (r.text)
        jsonData = json.loads(r.text)
        #print(len(jsonData['response']))
        
        mlist = []
        for i in range(0,len(jsonData['response'])):
            mlist.append(jsonData['response'][i]['fishtype'])
        
        return mlist