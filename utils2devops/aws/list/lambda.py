import json
import os

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
    if 'Concurrency' in conf:
        x.oreserved_concurrent_executions = \
            conf['Concurrency']['ReservedConcurrentExecutions']
    x.ovpc_config = None
    if 'Environment' in func:
        x.oenvironment = func['Environment']['Variables']
    x.okms_key_arn = None
    x.osource_code_hash = func["CodeSha256"]
    if 'Tags' in conf:
        x.otags = conf["Tags"]
    if 'VpcConfig' in func:
        if func['VpcConfig']['SubnetIds']:
            x.osubnet_ids = func['VpcConfig']['SubnetIds']
        if func['VpcConfig']['SecurityGroupIds']:
            x.osecurity_group_ids = func['VpcConfig']['SecurityGroupIds']

    if 'DEBUG_OR_IMPROVE' in os.environ:
        print('list_aliases')
        alias = client.list_aliases(FunctionName=func["FunctionArn"])
        for l in alias['Aliases']:
            print(l)
        print('list_event_source_mappings')
        event_source_mappings = client.list_event_source_mappings()
        for e in event_source_mappings['EventSourceMappings']:
            print(json.dumps(e, indent=4, sort_keys=True))
        print('list_layers')
        layers = client.list_layers()
        for l in layers['Layers']:
            print(json.dumps(l, indent=4, sort_keys=True))
            print('list_layer_versions')
            layer = client.list_layer_versions(LayerName=l['LayerName'])
            for v in layer['LayerVersions']:
                print(json.dumps(v, indent=4, sort_keys=True))
        print('list_tags')
        tags = client.list_tags(Resource=func["FunctionArn"])
        for t in tags['Tags']:
            print(json.dumps(t, indent=4, sort_keys=True))
        print('list_versions_by_function')
        versions_by_function = client.list_versions_by_function(
            FunctionName=func["FunctionArn"])
        for v in versions_by_function['Versions']:
            print(json.dumps(v, indent=4, sort_keys=True))
    print(x)
