import json 
import pandas as pd 

path = r".\dataFrance.json"

#function to load data

json_data = pd.read_json(path)

airQ=dict()
weather=dict()
location=dict()

airQ_list=[]
weather_list=[]
location_list=[]

_id=1
print(json_data)

def oulah():
    for row in json_data:
        #we identify by an id
        
        
        #airQ class
        airQ['id']=_id
        airQ['status']=json_data[row]['airQ']['status']  
        if(json_data[row]['airQ']['data'] == "Unknown station"):
            airQ['aqi'] = None
        else:
            airQ['aqi'] = json_data[row]['airQ']['data']['aqi']   
            airQ['time']= json_data[row]['airQ']['data']['time']['s']   
        
        #weather class
        weather['id']=_id
        weather['main']=json_data[row]['weather']['weather']['main']   
        weather['temp']=json_data[row]['weather']['main']['temp']   
        
        #location class
        
        location['id']=_id
        location['city']=json_data[row]['weather']['name']  

        location['longitude']=json_data[row]['weather']['coord']['lon']
        location['latitude']=json_data[row]['weather']['coord']['la']

        
        airQ_list.append(airQ)
        weather_list.append(weather)
        location_list.append(location)
        _id+=1

#print(airQ_list[0:10])
