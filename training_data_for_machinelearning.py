from sklearn import tree
import time
import json


time.localtime(time.time())
data = json.load(open('events.json'))

#Y = ['eventId', 'starttime', 'endtime', 'problem','severity', 'fixSuggestion', 'severtiy', 'snapshotId']
TRAINING_DATA = []

for i, event in enumerate(data):
	eventId = event.get("eventId")
	start = event.get("start")
	starttime = start / 1000
	starttimestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(starttime))
	starttimeparts = time.localtime(starttime)

	endtimeparts = time.localtime(endtime)
	end = event.get("end")
	endtime = end / 1000
	endtimestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(endtime))
	problem = event.get("problem")
	fixSuggestion = event.get("fixSuggestion")
	severtiy = event.get("severity")
	snapshotId = event.get("snapshotId")
	metrics = event.get("metrics")
	if(severtiy > 0):
		print(i, event, starttimeparts, endtimeparts)




#Problem Hour of Day, Day of Week,