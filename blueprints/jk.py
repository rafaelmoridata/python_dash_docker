#!/usr/bin/python3

import jenkins
from flask import Blueprint, render_template

jk = Blueprint('jk', __name__, url_prefix='/jenkins')

jc = jenkins.Jenkins('http://192.168.0.200:8080')

#dc = docker.DockerClient('tcp://192.168.0.200:2376')

@jk.route('')
def home():
	for job in jc.get_jobs():
		if job['name'] == 'Pipeline':
			pipeline = job
			break
	else:
		pipeline = {'name' : 'Nenhum job encontrado', 'color' : ''}
	pipeline['color'] = 'Construiu' if pipeline['color'] == 'blue' else 'Falhou'
	return render_template('jenkins.html', job=pipeline)