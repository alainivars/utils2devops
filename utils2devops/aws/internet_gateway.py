import boto3
import deprecation
from docs.version import __version__

from utils2devops.aws import InternetGateway

"""
Aws configuration files should be present:
 ~/.aws/credentials
 ~/.aws/config
"""


@deprecation.deprecated(deprecated_in='0.1.4', removed_in='0.2.0',
                        current_version=__version__,
                        details="Use $ aws apigateway get-rest-apis")
def list_internet_gateways(
        profile_name: str = 'terraform',
        region_name: str = 'us-east-1'
) -> [str]:
    """This function list all AWS Internet Gateways how can access the profile
    profile_name in the AWS region region_name.
    TODO
    :param profile_name: The AWS profile name to use.
    :param region_name: The AWS region to use.
    :returns: list of line or empty if nothing.
    :raises: AttributeError, KeyError

    """
    session = boto3.Session(profile_name=profile_name)
    client = session.client(service_name='ec2', region_name=region_name)
    elements = client.describe_internet_gateways()
    _lines = []
    for element in elements['InternetGateways']:
        x = InternetGateway(element['InternetGatewayId'])
        x.vpc_id = element['Attachments'][0]['VpcId']
        x.tags = element['Tags']
        _lines.append(x)
    return _lines


if __name__ == '__main__':
    lines = list_internet_gateways()
    print(*lines)
