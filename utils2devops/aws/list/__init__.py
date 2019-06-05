

class BlockTypeBase:
    """
    Describe at: https://www.terraform.io/docs/configuration/index.html
    Generate the base block type with the format:

    <BLOCK TYPE> "<BLOCK LABEL>" "<BLOCK NAME>" {
      # Block body
      <IDENTIFIER> = <EXPRESSION> # Argument
    }
    """
    def __init__(self, btype, label, name=''):
        self.type = btype
        self.label = label
        self.name = name

    def __str__(self):
        return self.type + ' "' + self.label + '" "' + self.name + '" {\n'


"""
Virtual Private Cloud
"""


class Vpc(BlockTypeBase):
    """

    """
    def __init__(self, name='') :
        super(Vpc, self).__init__(
            btype='resource', label='aws_vpc', name=name)
        self.cidr_block = ''
        self.enable_dns_hostnames = 'true'
        self.enable_dns_support = 'true'
        self.instance_tenancy = 'default'
        self.tags = []

    def __str__(self):
        the_str = super(Vpc, self).__str__()
        the_str += '\tcidr_block = "' + self.cidr_block + '"\n'
        the_str += '\tenable_dns_hostnames = '
        the_str += 'true\n' if self.enable_dns_hostnames else 'false\n'
        the_str += '\tenable_dns_support = '
        the_str += 'true\n' if self.enable_dns_support else 'false\n'
        the_str += '\tinstance_tenancy = "' + self.instance_tenancy + '"\n'
        the_str += '\n\ttags {\n'
        for tag in self.tags:
            the_str += '\t\t"' + tag['Key'] + '" = "' + tag['Value'] + '"\n'
        the_str += '\t}\n}\n\n'
        return the_str


class Subnet(BlockTypeBase):
    """

    """
    def __init__(self, name='') :
        super(Subnet, self).__init__(
            btype='resource', label='aws_subnet', name=name)
        self.vpc_id = ''
        self.cidr_block = ''
        self.availability_zone = ''
        self.map_public_ip_on_launch = True
        self.tags = []

    def __str__(self):
        if any('Name' in d['Key'] for d in self.tags):
            for tag in self.tags:
                if tag['Key'] == 'Name':
                    self.name = self.name + '-' + tag['Value']
                    break
        the_str = super(Subnet, self).__str__()
        the_str += '\tvpc_id = "' + self.vpc_id + '"\n'
        the_str += '\tcidr_block = "' + self.cidr_block + '"\n'
        the_str += '\tavailability_zone = "' + self.availability_zone + '"\n'
        the_str += '\tmap_public_ip_on_launch = '
        the_str += 'true\n' if self.map_public_ip_on_launch else 'false\n'
        the_str += '\n\ttags {\n'
        for tag in self.tags:
            the_str += '\t\t"' + tag['Key'] + '" = "' + tag['Value'] + '"\n'
        the_str += '\t}\n}\n'
        return the_str


class InternetGateway(BlockTypeBase):
    """

    """
    def __init__(self, name='') :
        super(InternetGateway, self).__init__(
            btype='resource', label='aws_internet_gateway', name=name)
        self.vpc_id = ''
        self.tags = []

    def __str__(self):
        the_str = super(InternetGateway, self).__str__()
        the_str += '\tvpc_id = "' + self.vpc_id + '"\n'
        the_str += '\n\ttags {\n'
        for tag in self.tags:
            the_str += '\t\t"' + tag['Key'] + '" = "' + tag['Value'] + '"\n'
        the_str += '\t}\n}\n\n'
        return the_str


class RouteTable(BlockTypeBase):
    """

    """
    def __init__(self, name='') :
        super(RouteTable, self).__init__(
            btype='resource', label='aws_route_table', name=name)
        self.vpc_id = ''
        self.route =  {
            'cidr_block': '',
            'gateway_id': '',
        }
        self.tags = []

    def __str__(self):
        the_str = super(RouteTable, self).__str__()
        the_str += '\tvpc_id = "' + self.vpc_id + '"\n'
        the_str += '\n\troute {\n'
        the_str += '\t\tcidr_block = "' + self.route['cidr_block'] + '"\n'
        the_str += '\t\tgateway_id = "' + self.route['gateway_id'] + '"\n\t}\n'
        the_str += '\n\ttags {\n'
        for tag in self.tags:
            the_str += '\t\t"' + tag['Key'] + '" = "' + tag['Value'] + '"\n'
        the_str += '\t}\n}\n'
        return the_str


"""
Security 
"""


class Gress:

    """

    """
    def __init__(self, name='') :
        self.rule_no = 100
        self.action = 'deny'
        self.cidr_block = "0.0.0.0/0"
        self.ipv6_cidr_block = ""
        self.protocol = "-1"
        self.from_port = 0
        self.to_port = 0
        self.icmp_code = 0
        self.icmp_type = 0

    def __str__(self):
        the_str = '\t\trule_no = "' + str(self.rule_no) + '"\n'
        the_str += '\t\taction = "' + self.action + '"\n'
        the_str += '\t\tcidr_block = "' + self.cidr_block + '"\n'
        the_str += '\t\tipv6_cidr_block = "' + self.ipv6_cidr_block + '"\n'
        the_str += '\t\tprotocol = "' + self.protocol + '"\n'
        the_str += '\t\tfrom_port = ' + str(self.from_port) + '\n'
        the_str += '\t\tto_port = ' + str(self.to_port) + '\n'
        the_str += '\t\ticmp_code = ' + str(self.icmp_code) + '\n'
        the_str += '\t\ticmp_type = ' + str(self.icmp_type) + '\n'
        return the_str


class NetworkAcl(BlockTypeBase):
    """

    """
    def __init__(self, name='') :
        super(NetworkAcl, self).__init__(
            btype='resource', label='aws_network_acl', name=name)
        self.vpc_id = ''
        self.subnet_ids = []
        self.ingress = []
        self.egress = []
        self.tags = []

    def __str__(self):
        if any('Name' in d['Key'] for d in self.tags):
            for tag in self.tags:
                if tag['Key'] == 'Name':
                    self.name = self.name + '-' + tag['Value']
                    break
        the_str = super(NetworkAcl, self).__str__()
        the_str += '\tvpc_id = "' + self.vpc_id + '"\n'
        the_str += '\tsubnet_ids = ['
        for tag in self.subnet_ids:
            the_str += '"' + tag + '",'
        the_str += ']\n\n'
        for i in self.ingress:
            the_str += '\tingress {\n'
            the_str += str(i)
            the_str += '\t}\n\n'
        for e in self.egress:
            the_str += '\tegress {\n'
            the_str += str(e)
            the_str += '\t}\n\n'
        the_str += '\ttags {\n'
        for tag in self.tags:
            the_str += '\t\t"' + tag['Key'] + '" = "' + tag['Value'] + '"\n'
        the_str += '\t}\n}\n'
        return the_str


class SecurityGroup(BlockTypeBase):
    """

    """
    def __init__(self, name='') :
        super(SecurityGroup, self).__init__(
            btype='resource', label='aws_security_group', name=name)
        self.name = ''
        self.description = ''
        self.vpc_id = ''
        self.ingress = []
        self.egress = []

    def __str__(self):
        the_str = super(SecurityGroup, self).__str__()
        the_str += '\tname = "' + self.name + '"\n'
        the_str += '\tdescription = "' + self.description + '"\n'
        the_str += '\tvpc_id = "' + self.vpc_id + '"\n'
        for i in self.ingress:
            the_str += '\n\tingress {\n'
            the_str += str(i)
            the_str += '\t}\n'
        for e in self.egress:
            the_str += '\n\tegress {\n'
            the_str += str(e)
            the_str += '\t}\n'
        the_str += '}\n'
        return the_str


"""
Lambda 
"""


class Lambda(BlockTypeBase):
    """
    https://www.terraform.io/docs/providers/aws/r/lambda_function.html
    """
    def __init__(self, name='') :
        super(Lambda, self).__init__(
            btype='resource', label='aws_lambda_function', name=name)
        self.ofilename = None
        self.os3_bucket = None
        self.os3_key = None
        self.os3_object_version = None
        self.function_name = ''
        self.odead_letter_config = None
        self.handler = ''
        self.role = ''
        self.odescription = None
        self.olayers = None
        self.omemory_size = None
        self.runtime = ''
        self.otimeout = None
        self.oreserved_concurrent_executions = None
        self.opublish = None
        self.ovpc_config = None
        self.oenvironment = None
        self.okms_key_arn = None
        self.osource_code_hash = None
        self.otags = None
        self.otarget_arn = None
        self.osubnet_ids = None
        self.osecurity_group_ids = None

    def __str__(self):
        the_str = super(Lambda, self).__str__()
        if self.ofilename:
            the_str += '\tfilename = "' + self.ofilename + '"\n'
        if self.os3_bucket:
            the_str += '\ts3_bucket = "' + self.os3_bucket + '"\n'
        if self.os3_key:
            the_str += '\ts3_key = "' + self.os3_key + '"\n'
        if self.os3_object_version:
            the_str += '\ts3_object_version = "' + self.os3_object_version + '"\n'
        the_str += '\tfunction_name = "' + self.function_name + '"\n'
        if self.odead_letter_config:
            the_str += '\tdead_letter_config = "' + self.odead_letter_config + '"\n'
        the_str += '\thandler = "' + self.handler + '"\n'
        the_str += '\trole = "' + self.role + '"\n'
        if self.odescription:
            the_str += '\tdescription = "' + self.odescription + '"\n'
        if self.olayers:
            the_str += '\tlayers = {' + self.olayers + '"\n'
            for layer in self.olayers:
                the_str += '\t\t"' + layer['Key'] + '" = "' + layer['Value'] + '"\n'
            the_str += '\t}\n'
        if self.omemory_size:
            the_str += '\tmemory_size = "' + str(self.omemory_size) + '"\n'
        the_str += '\truntime = "' + self.runtime + '"\n'
        if self.otimeout:
            the_str += '\ttimeout = "' + str(self.otimeout) + '"\n'
        if self.oreserved_concurrent_executions:
            the_str += '\treserved_concurrent_executions = "' + \
                       str(self.oreserved_concurrent_executions) + '"\n'
        if self.opublish:
            the_str += '\tpublish = "' + self.opublish + '"\n'
        if self.ovpc_config:
            the_str += '\tvpc_config = "' + self.ovpc_config + '"\n'
        if self.oenvironment:
            the_str += '\tenvironment {\n'
            the_str += '\n\tvariables = {\n'
            for k, v in self.oenvironment.items():
                the_str += '\t\t"' + k + '" = "' + v + '"\n'
            the_str += '\t}\n'
        if self.okms_key_arn:
            the_str += '\tkms_key_arn = "' + self.okms_key_arn + '"\n'
        if self.osource_code_hash:
            the_str += '\tsource_code_hash = "' + self.osource_code_hash + '"\n'
        if self.otags:
            the_str += '\ttags {\n'
            for k, v in self.otags.items():
                the_str += '\t\t"' + k + '" = "' + v + '"\n'
            the_str += '\t}\n'
        if self.otarget_arn:
            the_str += '\ttarget_arn = "' + self.otarget_arn + '"\n'
        if self.osubnet_ids:
            the_str += '\tsubnet_ids = "' + self.osubnet_ids + '"\n'
        if self.osecurity_group_ids:
            the_str += '\tsecurity_group_ids = "' + self.osecurity_group_ids + '"\n'
        the_str += '}\n'
        return the_str


"""
S3 
"""


class S3Bucket(BlockTypeBase):
    """
    https://www.terraform.io/docs/providers/aws/r/s3_bucket.html
    """
    def __init__(self, name='') :
        super(S3Bucket, self).__init__(
            btype='resource', label='aws_lambda_function', name=name)
        self.bucket = None
        self.acl = None
        self.versioning = None

    def __str__(self):
        the_str = super(S3Bucket, self).__str__()
        the_str += '\tbucket = "' + self.bucket + '"\n'
        if self.acl:
            the_str += '\tacl = "' + self.acl + '"\n'
        if self.versioning:
            the_str += '\tversioning {\n\t\tenabled = ' + self.versioning + '\n\t}\n'
        the_str += 'TODO\n'
        the_str += '}\n'
        return the_str



