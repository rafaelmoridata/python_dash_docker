#!/usr/bin/python3

import boto3

ec2 = boto3.resource("ec2")

#security_group = ec2.create_security_group(GroupName='GrupoScript', Description='Criado por script')
#print(security_group)

security_group = ec2.SecurityGroup('sg-08c055d0a1cf')

#for group in security_groups:
#	print(group.group_name, group.group_id)

security_group.authorize_ingress(
	FromPort=80,
	ToPort=80,
	CidrIp='0.0.0.0/0',
	IpProtocol='tcp'
)

security_group.revoke_ingress(
	FromPort=80,
	ToPort=80,
	CidrIp='0.0.0.0/0',
	IpProtocol='tcp'
)	

security_group.delete()

