from urllib.request import urlopen, Request
import json

dict= {'token': '607bda74035d00a7cbd96390269808d2'}


request = Request('http://challenge.code2040.org/api/prefix')
request.add_header('Content-Type', 'application/json')

response = urlopen(request, json.dumps(dict).encode('utf8'))

pref = json.loads(response.read().decode('utf8'))#decodes http response and loads it as a dictionary

array = []

for i in pref['array']:
    if not i.startswith(pref['prefix']):
        array.append(i)

dict['array'] = array
request = Request('http://challenge.code2040.org/api/prefix/validate')
request.add_header('Content-Type', 'application/json')

response = urlopen(request, json.dumps(dict).encode('utf8'))
