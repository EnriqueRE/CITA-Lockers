import json
# import urllib
#import urllib2
import time
import requests
import csv


start_time = time.time()

csvFile = csv.reader(open('G:\Users\Agustin de la Rocha\Desktop\Audit_Trail', 'rb'))

url_event = "http://192.168.2.13:8000/api/v1/Event/"
url_zone = "http://192.168.2.13:8000/api/v1/Zone/"

headers = {'Content-type': 'application/json'}

erase = requests.delete(url_event, headers = headers)

newFile = []
areaList = set()
newList = []
lockerList = []
closed = 0

rows = list(csvFile)
totalrows = len(rows)
print totalrows

for i in reversed(rows):
	newFile.append(i)

for row in rows:
	#if row[3] not in areaList:
		newList.append(row)

		if row[5] not in areaList:
			areaList.add(row[5])

		values = {"locker": row[4], "name": row[3], "resource_uri": "/api/v1/Event/1/", "usergpf1": row[2], "zone": row[5], "date": row[0], "Description": row[1]}

		req = requests.post(url_event, data = json.dumps(values), headers = headers) 

for Area in areaList:
	for row in newFile:
		if Area == row[5]:
			if row[4] not in lockerList:
				lockerList.append(row[4])
				if row[1] == "Door closed (key)":
					closed += 1
	print closed
	req = requests.get(url_zone + Area)
	j = req.json()
	#data = json.loads(j)
	total = int(j['total'])
	#print data
	free = total - closed
	values = {"closed": closed, "free": free}
	req = requests.put(url_zone + Area + "/", data = json.dumps(values), headers = headers)
	closed = 0

print areaList
print newList

print time.time() - start_time, "seconds"