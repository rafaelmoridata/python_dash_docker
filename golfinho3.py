#!/usr/bin/python3

import boto3

ec2 = boto3.resource("ec2")

#stop_instance = ec2.instances.filter(InstanceIds=['i-01b50b2feeff408da']).stop()
start_instance = ec2.instances.filter(InstanceIds=['i-01b50b2feeff408da']).terminate()
	
