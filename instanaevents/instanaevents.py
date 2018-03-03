import json
import urllib3
import time
import datetime



http = urllib3.PoolManager()

def get_instana_event_data():
	data = json.load(open('events.json'))
	return data

def get_instana_training_data():
	data = json.load(open('events_train.json'))


def get_remote_events():
	results = http.request('GET', 'https://current-instana.instana.io/api/events',
	headers = {	'Authorization': 'apitoken XXXXXXXXXXXXXXX'})
	moredata = json.loads(results.data.decode('utf-8'))
	return moredata



my = get_remote_events()




localtime = time.localtime(time.time())
currenttime = time.time()


onehour = 3600000
oneday = 86400000
oneweek = 604800000


print(currenttime)
print(localtime)
print( 'Now    :', datetime.datetime.now())
print( 'Today  :', datetime.datetime.today())
print('UTC Now:', datetime.datetime.utcnow())








