import time
import json
from urllib.request import urlopen, Request
from datetime import timedelta
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


dict= {'token': '607bda74035d00a7cbd96390269808d2'}

request = Request('http://challenge.code2040.org/api/dating')
request.add_header('Content-Type', 'application/json')
response = urlopen(request, json.dumps(dict).encode('utf8'))

timedict = json.loads(response.read().decode('utf8'))#decodes http response and loads it as a dictionary

parsed = parse(timedict['datestamp'])#takes time from dictionary and converts to a datetime object
parsed += relativedelta(seconds=timedict['interval'])#adds seconds to the time
parsed = parsed.isoformat()[:19] + 'Z' #this Z is added to indicate UTC time

dict['datestamp'] = parsed

request = Request('http://challenge.code2040.org/api/dating/validate')
request.add_header('Content-Type', 'application/json')
response = urlopen(request, json.dumps(dict).encode('utf8'))
