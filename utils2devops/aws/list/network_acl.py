import boto3

from utils2devops.aws.list import NetworkAcl, Gress

"""
Aws configuration iiles should be present:
 ~/.aws/credentials
 ~/.aws/config
"""
session = boto3.Session(profile_name='terraform')
client = session.client(service_name='ec2', region_name='us-east-2')
elements = client.describe_network_acls()

for element in elements['NetworkAcls']:
    x = NetworkAcl(element['NetworkAclId'])
    x.vpc_id = element['VpcId']
    x.subnet_ids = []
    for p in element['Associations']:
        x.subnet_ids.append(p['SubnetId'])
    for p in element['Entries']:
        if p['RuleNumber'] != 32767:
            gress = Gress()
            gress.rule_no = p['RuleNumber']
            gress.action = p['RuleAction']
            gress.cidr_block = p['CidrBlock']
            gress.protocol = p['Protocol']
            if 'PortRange' in p:
                gress.from_port = p['PortRange']['From']
                gress.to_port = p['PortRange']['To']
            else:
                gress.from_port = 0
                gress.to_port = 0
            if p['Egress']:
                x.egress.append(gress)
            else:
                x.ingress.append(gress)
    x.tags = element['Tags']
    print(x)
