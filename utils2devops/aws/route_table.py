import boto3

from utils2devops.aws import RouteTable, Route, RouteTableAssociation

"""
Aws configuration iiles should be present:
 ~/.aws/credentials
 ~/.aws/config
"""


def list_route_tables(
        profile_name: str = 'terraform',
        region_name: str = 'us-east-1'
) -> [str]:
    """This function list all AWS Internet Gateways how can access the profile
    profile_name in the AWS region region_name.

    :param profile_name: The AWS profile name to use.
    :param region_name: The AWS region to use.
    :returns: list of line or empty if nothing.
    :raises: AttributeError, KeyError

    """
    session = boto3.Session(profile_name=profile_name)
    client = session.client(service_name='ec2', region_name=region_name)
    elements = client.describe_route_tables()
    _lines = []

    for element in elements['RouteTables']:
        x = RouteTable()
        x.vpc_id = element['VpcId']
        x.route_table_id = element['RouteTableId']
        for route in element['Routes']:
            r = Route()
            r.route_table_id = x.route_table_id
            r.destination_cidr_block = route['DestinationCidrBlock'] if 'DestinationCidrBlock' in route else None
            r.destination_ipv6_cidr_block = route['DestinationCidrIpv6Block'] if 'DestinationCidrIpv6Block' in route else None
            r.egress_only_gateway_id = route['EgressOnlyGatewayId'] if 'EgressOnlyGatewayId' in route else None
            r.gateway_id = route['GatewayId'] if 'GatewayId' in route else None
            r.instance_id = route['InstanceId'] if 'InstanceId' in route else None
            r.nat_gateway_id = route['NatGatewayId'] if 'NatGatewayId' in route else None
            r.network_interface_id = route['NetworkInterfaceId'] if 'NetworkInterfaceId' in route else None
            r.transit_gateway_id = route['TransitGatewayId'] if 'TransitGatewayId' in route else None
            r.vpc_peering_connection_id = route['VpcPeeringConnectionId'] if 'VpcPeeringConnectionId' in route else None
            x.routes.append(r)
        for association in element['Associations']:
            if association.get('SubnetId', None):
                a = RouteTableAssociation()
                a.subnet_id = association['SubnetId']
                a.route_table_id = association['RouteTableId']
                _lines.append(a)

        x.tags = element['Tags']
        _lines.append(x)

    return _lines


if __name__ == '__main__':
    lines = list_route_tables()
    print(*lines)
