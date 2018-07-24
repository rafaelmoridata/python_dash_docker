#!/usr/bin/python3

import requests

TOKEN = 'jBrzeuh42xn_a8rM-uhm'
GITLAB = 'http://192.168.0.100/api/v4/{route}?private_token={tk}'

response = requests.get(GITLAB.format(tk=TOKEN, route='projects'))
print(response.json()) 
exit()

#response = requests.get(GITLAB.format(tk=TOKEN))
#print(response.json())

#repository = {'name' : 'flask-app'}
#response = requests.post(GITLAB.format(tk=TOKEN, route='projects'), repository)
#print(response.json())

#response = requests.get(GITLAB.format(tk=TOKEN, route='users'))
#for user in response.json():
#	print(user['name'])

#user = {'email' : 'paramahansa@yogananda.co.uk',
#	    'username' : 'paragananda',
#	    'name' : 'Paramahansa Yogananda',
#	    'password' : 'papagogo123'}

#response = requests.post(GITLAB.format(tk=TOKEN, route='users'), user)
#print(response.json())

pid = 2
response = requests.post('http://192.168.0.100/api/v4/projects/{pid}/members?private_token={tk}'.format(pid=2, tk=TOKEN))
