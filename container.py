#!/usr/bin/python3

import docker

dc = docker.DockerClient('tcp://192.168.0.200:2376')

c = dc.containers.run('flask-app', '/bin/bash', name='impostor', detach=True, tty=True, ports={'9191':'80'})
print(c)

print('{0:.<25}|{1:.<30}|{2:.>10}'.format('NOME', 'IMAGE', 'STATUS'))
for c in dc.containers.list(all=True):
    if c.status == 'exited':
        c.remove()
        continue
    tag = c.image.tags[0]
    print('{0:.<25}|{1:.>30}|{2:.>10}'.format(c.name, tag, c.status))

flask_app = dc.containers.get('flask-app')
output = flask_app.exec_run(['ls', '-l', '/php'], tty=True).output

for line in output.decode('utf-8').split('\n'):
    print(line)
