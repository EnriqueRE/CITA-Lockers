import json
import time
import requests
import csv


start_time = time.time()

csvFile = csv.reader(open('/Users/luishoracio/PycharmProjects/CITA-Lockers/Documentacion/Audit_Trail', 'rb'))

ip_address = "http://127.0.0.1:8000"

url_event = ip_address + "/api/v1/Event/"
url_zone = ip_address + "/api/v1/LockerZone/"

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
		newList.append(row)

		if row[5] not in areaList:
			areaList.add(row[5])

		values = {"locker": row[4], "name": row[3], "resource_uri": "/api/v1/Event/1/", "usergpf1": row[2], "zone": row[5], "date": row[0], "description": row[1]}

		req = requests.post(url_event, data = json.dumps(values), headers = headers) 

"""for Area in areaList:
	for row in newFile:
		if Area == row[5]:
			if row[4] not in lockerList:
				lockerList.append(row[4])
				if row[1] == "Door closed (key)":
					closed += 1
	print closed
	req = requests.get(url_zone + Area)
	j = req.json()
	total = int(j['total'])
	free = total - closed
	values = {"occupied": closed, "free": free}
	req = requests.put(url_zone + Area + "/", data = json.dumps(values), headers = headers)
	closed = 0"""

print areaList
print newList

print time.time() - start_time, "seconds"