#!/usr/bin/python3

import boto3

ec2 = boto3.resource("ec2")

instances = ec2.instances.all()
for c in instances:
	print(c.instance_id)
	print(c.instance_type)


	
