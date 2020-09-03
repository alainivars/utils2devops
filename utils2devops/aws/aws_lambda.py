import json
import os

import boto3

from utils2devops.aws import Lambda

"""
Aws configuration iiles should be present:
 ~/.aws/credentials
 ~/.aws/config
"""


def list_lambda_function(
        profile_name: str = 'terraform',
        region_name: str = 'us-east-1'
) -> [str]:
    """This function list all AWS lambda how can access the profile
    profile_name in the AWS region region_name.

    :param profile_name: The AWS profile name to use.
    :param region_name: The AWS region to use.
    :returns: list of line or empty if nothing.
    :raises: AttributeError, KeyError

    """
    session = boto3.Session(profile_name=profile_name)
    client = session.client(service_name='lambda', region_name=region_name)
    functions = client.list_functions()

    _lines = []
    if 'Functions' not in functions:
        return _lines
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
            x.tags = conf["Tags"]
        if 'VpcConfig' in func:
            if func['VpcConfig']['SubnetIds']:
                x.osubnet_ids = func['VpcConfig']['SubnetIds']
            if func['VpcConfig']['SecurityGroupIds']:
                x.osecurity_group_ids = func['VpcConfig']['SecurityGroupIds']

        if 'DEBUG_OR_IMPROVE' in os.environ:
            print('list_aliases')
            alias = client.list_aliases(FunctionName=func["FunctionArn"])
            for al in alias['Aliases']:
                print(al)
            print('list_event_source_mappings')
            event_source_mappings = client.list_event_source_mappings()
            for event_source_mapping in event_source_mappings['EventSourceMappings']:
                print(json.dumps(event_source_mapping, indent=4, sort_keys=True))
            print('list_layers')
            layers = client.list_layers()
            for layer in layers['Layers']:
                print(json.dumps(layer, indent=4, sort_keys=True))
                print('list_layer_versions')
                layer_versions = client.list_layer_versions(LayerName=layer['LayerName'])
                for version in layer_versions['LayerVersions']:
                    print(json.dumps(version, indent=4, sort_keys=True))
            print('list_tags')
            tags = client.list_tags(Resource=func["FunctionArn"])
            for tag in tags['Tags']:
                print(json.dumps(tag, indent=4, sort_keys=True))
            print('list_versions_by_function')
            versions_by_function = client.list_versions_by_function(
                FunctionName=func["FunctionArn"])
            for version in versions_by_function['Versions']:
                print(json.dumps(version, indent=4, sort_keys=True))

        _lines.append(x)

    return _lines


if __name__ == '__main__':
    lines = list_lambda_function()
    print(*lines)
