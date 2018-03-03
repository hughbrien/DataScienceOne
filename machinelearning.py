

from sklearn import tree


import numpy
import scipy
import time

import json
from pprint import pprint


time.localtime(time.time())

data = json.load(open('events_train.json'))

#Y = ['eventId', 'starttime', 'endtime', 'problem','severity', 'fixSuggestion', 'severtiy', 'snapshotId']
TRAINING_DATA = []

for i, event in enumerate(data):
	eventId = event.get("eventId")
	start = event.get("start")
	starttime = start / 1000
	starttimestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(starttime))
	end = event.get("end")
	endtime = end / 1000
	endtimestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(endtime))
	problem = event.get("problem")
	fixSuggestion = event.get("fixSuggestion")
	severtiy = event.get("severity")
	snapshotId = event.get("snapshotId")
	metrics = event.get("metrics")
	if(metrics is None):
		metrics = "No Metrics"
	else:
		metrics = event.get("metrics")
		#TRAINING_DATA.append([i, eventId, starttimestr, endtimestr, problem,  fixSuggestion, severtiy, snapshotId])
	TRAINING_DATA.append([i, starttime, endtime, severtiy])
#End of for

print(TRAINING_DATA)

Y = ['Ignore','Ignore','Ignore','Ignore','Ignore','Ignore','Ignore','Ignore','Ignore','Ignore','Ignore','Important','Important','Important']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(TRAINING_DATA, Y)
print(clf)

prediction = clf.predict([[0, 1513782236.0, 1513782237.0, -1],
						  [100, 1519927709.0, 1519927902.075, 10],
						  [100, 1519927709.0, 1519927902.075, 5],
						  [0, 1519927709.0, 1519927902.075, -1]])

print(prediction)