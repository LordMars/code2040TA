from urllib.request import urlopen, Request
import json

dict= {'token': '607bda74035d00a7cbd96390269808d2'}


request = Request('http://challenge.code2040.org/api/reverse')
request.add_header('Content-Type', 'application/json')

response = urlopen(request, json.dumps(dict).encode('utf8'))

dict['string'] = (response.read()[::-1]).decode('utf8')#reads given string, reverses and decodes it, and stores it in dict

request = Request('http://challenge.code2040.org/api/reverse/validate')
request.add_header('Content-Type', 'application/json')

response = urlopen(request, json.dumps(dict).encode('utf8'))