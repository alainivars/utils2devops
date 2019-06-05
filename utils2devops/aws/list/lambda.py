import boto3

from utils2devops.aws.list import Lambda

"""
Aws configuration iiles should be present:
 ~/.aws/credentials
 ~/.aws/config
"""
session = boto3.Session(profile_name='terraform')
client = session.client(service_name='lambda', region_name='us-east-2')
functions = client.list_functions()

for func in functions["Functions"]:
    x = Lambda(func["FunctionName"])
    conf = client.get_function(FunctionName=func["FunctionArn"])
    x.function_name = func["FunctionName"]
    x.handler = func["Handler"]
    x.role = func["Role"]
    x.odescription = func["Description"]
    x.omemory_size = func["MemorySize"]
    x.runtime = func["Runtime"]
    x.otimeout = func["Timeout"]
    x.oreserved_concurrent_executions = \
        conf['Concurrency']['ReservedConcurrentExecutions']
    x.ovpc_config = None
    if 'Environment' in func:
        x.oenvironment = func['Environment']['Variables']
    x.okms_key_arn = None
    x.osource_code_hash = func["CodeSha256"]
    if 'Tags' in conf:
        x.otags = conf["Tags"]
    if func['VpcConfig']['SubnetIds']:
        x.osubnet_ids = func['VpcConfig']['SubnetIds']
    if func['VpcConfig']['SecurityGroupIds']:
        x.osecurity_group_ids = func['VpcConfig']['SecurityGroupIds']
    print(x)
