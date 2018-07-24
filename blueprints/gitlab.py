#!/usr/bin/python3

import requests
from flask import Blueprint, render_template

gitlab = Blueprint('gitlab', __name__, url_prefix='/gitlab')

TOKEN = 'jBrzeuh42xn_a8rM-uhm'
GITLAB = 'http://192.168.0.100/api/v4/{route}?private_token={tk}'

#jc = jenkins.Jenkins('http://192.168.0.200:8080')

#dc = docker.DockerClient('tcp://192.168.0.200:2376')

@gitlab.route('')
def home():
	users = requests.get(GITLAB.format(tk=TOKEN, route='users'))
	projects = requests.get(GITLAB.format(tk=TOKEN, route='projects'))	
	#print(projects.json())
	return render_template('gitlab.html', users=users.json(), projects=projects.json())
