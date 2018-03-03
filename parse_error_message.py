import time
import json
import nltk



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

	end = event.get("end")
	endtime = end / 1000
	endtimestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(endtime))
	endtimeparts = time.localtime(endtime)

	problem = event.get("problem")
	fixSuggestion = event.get("fixSuggestion")
	severtiy = event.get("severity")
	snapshotId = event.get("snapshotId")
	metrics = event.get("metrics")

	problem_tokens = nltk.word_tokenize(problem)
	fixSuggestion_tokens = nltk.word_tokenize(fixSuggestion)




	if(severtiy > 0):
		print(i, problem_tokens, fixSuggestion_tokens, event)

#Problem Hour of Day, Day of Week,