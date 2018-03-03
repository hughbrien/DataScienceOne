import time
import json
import datetime
from sklearn import tree
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


import instanaevents.instanaevents as ev

time.localtime(time.time())

data =  ev.get_instana_event_data()


#Y = ['eventId', 'starttime', 'endtime', 'problem','severity', 'fixSuggestion', 'severtiy', 'snapshotId']
TRAINING_DATA = []
HOURS = []
DAYOFWEEK = []
SEVERITY = []


for i, event in enumerate(data):
	eventId = event.get("eventId")
	start = event.get("start")
	starttime = start / 1000
	starttimestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(starttime))
	starttimeparts = time.localtime(starttime)

	end = event.get("end")
	endtime = end / 1000
	endtimestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(endtime))
	endtimeparts = time.localtime(endtime)

	endhour = endtimeparts.tm_hour
	endmin = endtimeparts.tm_hour
	endmonth = endtimeparts.tm_mon
	endmday = endtimeparts.tm_mday
	endtimezone = endtimeparts.tm_zone
	enddayofweek = endtimeparts.tm_wday
	endjday = endtimeparts.tm_yday
	endyear = endtimeparts.tm_year

	starthour = starttimeparts.tm_hour
	startmin = starttimeparts.tm_hour
	startmday = starttimeparts.tm_mday
	startmonth = starttimeparts.tm_mon
	starttimezone = starttimeparts.tm_zone
	startdayofweek = starttimeparts.tm_wday
	startjday = starttimeparts.tm_yday
	startyear = starttimeparts.tm_year

	problem = event.get("problem")
	fixSuggestion = event.get("fixSuggestion")
	severtiy = event.get("severity")
	snapshotId = event.get("snapshotId")
	metrics = event.get("metrics")
	HOURS.append(starthour)
	DAYOFWEEK.append(startdayofweek)
	SEVERITY.append(abs(severtiy))




print(HOURS)
print(DAYOFWEEK)
print(SEVERITY)

sns.distplot(HOURS)
plt.show()


