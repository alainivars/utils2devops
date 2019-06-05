import boto3

from utils2devops.aws.list import InternetGateway

"""
Aws configuration iiles should be present:
 ~/.aws/credentials
 ~/.aws/config
"""
session = boto3.Session(profile_name='terraform')
client = session.client(service_name='ec2', region_name='us-east-2')
elements = client.describe_internet_gateways()

for element in elements['InternetGateways']:
    x = InternetGateway(element['InternetGatewayId'])
    x.vpc_id = element['Attachments'][0]['VpcId']
    x.tags = element['Tags']
    print(x)
