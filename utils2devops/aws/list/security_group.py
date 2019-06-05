import boto3

from utils2devops.aws.list import SecurityGroup, Gress

"""
Aws configuration iiles should be present:
 ~/.aws/credentials
 ~/.aws/config
"""
session = boto3.Session(profile_name='terraform')
client = session.client(service_name='ec2', region_name='us-east-2')
elements = client.describe_security_groups()

for element in elements['SecurityGroups']:
    x = SecurityGroup(element['GroupId'])
    x.name = element['GroupName']
    x.description = element['Description']
    x.vpc_id = element['VpcId']
    for p in element['IpPermissions']:
        gress = Gress()
        gress.protocol = p['IpProtocol']
        if 'PortRange' in p:
            gress.from_port = p['FromPort']
            gress.to_port = p['ToPort']
        else:
            gress.from_port = 0
            gress.to_port = 0
        gress.cidr_block = p['IpRanges'][0]['CidrIp'] if len(p['IpRanges']) else ''
        x.ingress.append(gress)
    for p in element['IpPermissionsEgress']:
        gress = Gress()
        gress.protocol = p['IpProtocol']
        if 'PortRange' in p:
            gress.from_port = p['FromPort']
            gress.to_port = p['ToPort']
        else:
            gress.from_port = 0
            gress.to_port = 0
        gress.cidr_block = p['IpRanges'][0]['CidrIp'] if len(p['IpRanges']) else ''
        x.egress.append(gress)
    print(x)
