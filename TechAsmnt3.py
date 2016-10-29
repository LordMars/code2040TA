from urllib.request import urlopen, Request
import json

dict= {'token': '607bda74035d00a7cbd96390269808d2'}


request = Request('http://challenge.code2040.org/api/haystack')
request.add_header('Content-Type', 'application/json')

response = urlopen(request, json.dumps(dict).encode('utf8'))

stack = json.loads(response.read().decode('utf8'))#decodes http response and loads it as a dictionary

for i in range(len(stack['haystack'])):
    if stack['needle'] == stack['haystack'][i]:
        dict['needle'] = i

request = Request('http://challenge.code2040.org/api/haystack/validate')
request.add_header('Content-Type', 'application/json')

response = urlopen(request, json.dumps(dict).encode('utf8'))
