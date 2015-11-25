import json
data = []
data_name = 'data.json'
statistic = {}

try:
	json_data=open(data_name)
	data = json.load(json_data)
except:
	print ("Not find file with name %s" % data_name)

for d in data:
 	if d['unit'] in statistic:
 		statistic[d['unit']]+=1
 	else:
 		statistic[d['unit']]=1

for s in statistic:
	print s, statistic[s]




