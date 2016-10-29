from urllib.request import urlopen, Request
import json

dict= {'token': '607bda74035d00a7cbd96390269808d2', 
        'github': 'https://github.com/LordMars/code2040TA'}


request = Request('http://challenge.code2040.org/api/register')
request.add_header('Content-Type', 'application/json')
request.add_header('Connection', 'close')

response = urlopen(request, json.dumps(dict).encode('utf8'))
