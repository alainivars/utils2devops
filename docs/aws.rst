
.. include:: links.inc

.. _ref-create-profile:

Aws Tools
=========

Create an AWS account (it's free)::

    https://aws.amazon.com/

Aws secret required, create a ~/.aws/credential file and add::

    [default]
    aws_access_key_id = <Your key id>
    aws_secret_access_key = <Your secret access key id>
    [terraform]
    aws_access_key_id = <Your key id>
    aws_secret_access_key = <Your secret access key id>

Aws Env required, create a ~/.aws/config file and add::

    [default]
    output = json
    region = <the region name>
    [terraform]
    output = json
    region = <the region name>


WARNING: Deprecated in version 0.2.0, now provided by AWS directly :)
=====================================================================
https://docs.aws.amazon.com/cli/latest/index.html

EXEMPLE::

    PYTHONPATH=. python utils2devops/aws/internet_gateway.py
    resource "aws_internet_gateway" "igw-8bc0adef" {
        vpc_id = "vpc-4a50ae2d"
        tags {
        }
    }

    aws apigateway get-rest-apis
    {
        "items": [
            {
                "id": "823ja68abi",
                "name": "serverlessrepo-api-gatewa-apigatewayauthorizerpyth-XL8UW8JQXOBJ-API",
                "description": "Created by AWS Lambda",
                "createdDate": "2019-06-06T09:38:20+00:00",
                "apiKeySource": "HEADER",
                "endpointConfiguration": {
                    "types": [
                        "REGIONAL"
                    ]
                }
            }
        ]
    }



List Api Gateway
----------------
To list all the api gateway for the region::

    PYTHONPATH=. python utils2devops/aws/api_gateway_v2.py


List Aws lambda
---------------
To list all the Aws lambda for the region::

    PYTHONPATH=. python utils2devops/aws/aws_lambda.py

List internet gateway
---------------------
To list all the internet gateway for the region::

    PYTHONPATH=. python utils2devops/aws/internet_gateway.py

    resource "aws_internet_gateway" "igw-9935f0" {
        vpc_id = "vpc-9e987"
        tags {
        }
    }

List lambda ssm
---------------
To list all the lambda ssm for the region::

    PYTHONPATH=. python utils2devops/aws/lambda_ssm.py

List network acl
----------------
To list all the network acl for the region::

    $ PYTHONPATH=. python utils2devops/aws/network_acl.py
    resource "aws_network_acl" "acl-c31fc4a4" {
        vpc_id = "vpc-4a50ae2d"
        subnet_ids = ["subnet-35dfb76d","subnet-09a73005","subnet-bdedb380","subnet-a35833c6","subnet-e392f0c9","subnet-ad0e52db",]
        ingress {
            rule_no = "100"
            action = "allow"
            cidr_block = "0.0.0.0/0"
            ipv6_cidr_block = ""
            protocol = "-1"
            from_port = 0
            to_port = 0
            icmp_code = 0
            icmp_type = 0
        }
        egress {
            rule_no = "100"
            action = "allow"
            cidr_block = "0.0.0.0/0"
            ipv6_cidr_block = ""
            protocol = "-1"
            from_port = 0
            to_port = 0
            icmp_code = 0
            icmp_type = 0
        }
        tags {
        }
    }

    // BY AWS CLI directly
    $ aws ec2 describe-network-acls
    {
        "NetworkAcls": [
            {
                "Associations": [
                    {
                        "NetworkAclAssociationId": "aclassoc-8149f6e9",
                        "NetworkAclId": "acl-f1780b98",
                        "SubnetId": "subnet-a308c3ee"
                    },
                    {
                        "NetworkAclAssociationId": "aclassoc-8f49f6e7",
                        "NetworkAclId": "acl-f1780b98",
                        "SubnetId": "subnet-83a3dfea"
                    },
                    {
                        "NetworkAclAssociationId": "aclassoc-8049f6e8",
                        "NetworkAclId": "acl-f1780b98",
                        "SubnetId": "subnet-345ce64f"
                    }
                ],
                "Entries": [
                    {
                        "CidrBlock": "0.0.0.0/0",
                        "Egress": true,
                        "PortRange": {
                            "From": 80,
                            "To": 80
                        },
                        "Protocol": "6",
                        "RuleAction": "allow",
                        "RuleNumber": 100
                    },
                    {
                        "CidrBlock": "0.0.0.0/0",
                        "Egress": true,
                        "Protocol": "-1",
                        "RuleAction": "deny",
                        "RuleNumber": 32767
                    },
                    {
                        "CidrBlock": "0.0.0.0/0",
                        "Egress": false,
                        "PortRange": {
                            "From": 443,
                            "To": 443
                        },
                        "Protocol": "6",
                        "RuleAction": "allow",
                        "RuleNumber": 100
                    },
                    {
                        "CidrBlock": "0.0.0.0/0",
                        "Egress": false,
                        "Protocol": "-1",
                        "RuleAction": "deny",
                        "RuleNumber": 32767
                    }
                ],
                "IsDefault": true,
                "NetworkAclId": "acl-f1780b98",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "network-acl-name"
                    }
                ],
                "VpcId": "vpc-9e98f6f7",
                "OwnerId": "397270606208"
            }
        ]
    }


List route table
----------------
To list all the route table for the region::

    PYTHONPATH=. python utils2devops/aws/route_table.py

    resource "aws_route_table" "" {
        vpc_id = "vpc-4a50ae2d"

        route {
            route_table_id = "rtb-6298e405"
            destination_cidr_block = "172.31.0.0/16"
            gateway_id = "local"
        }

        route {
            route_table_id = "rtb-6298e405"
            destination_cidr_block = "0.0.0.0/0"
            gateway_id = "igw-8bc0adef"
        }
    }

List s3 bucket
--------------
To list all the s3 bucket for the region::

    PYTHONPATH=. python utils2devops/aws/s3_bucket.py

List secret
-----------
To list all the secret for the region::

    PYTHONPATH=. python utils2devops/aws/secretmanager.py

List security group
-------------------
To list all the security group for the region::

    PYTHONPATH=. python utils2devops/aws/security_group.py

List ssm
--------
To list all the ssm for the region::

    PYTHONPATH=. python utils2devops/aws/ssm.py

List subnet
-----------
To list all the subnet for the region::

    PYTHONPATH=. python utils2devops/aws/subnet.py

List vpc
--------
To list all the vpc for the region::

    PYTHONPATH=. python utils2devops/aws/vpc.py

