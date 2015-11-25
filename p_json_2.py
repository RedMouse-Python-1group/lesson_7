import os
import json
json_data=open('struct.json','w')
json.dump(os.listdir(os.getcwd()),json_data)
json_data.close() 
