
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


List Api Gateway
----------------

To list all the api gateway for the region::

    PYTHONPATH=. python utils2devops/aws/network_acl.py

    resource "aws_network_acl" "acl-06807accba82" {
        vpc_id = "vpc-0b4bc90e75638"
        subnet_ids = ["subnet-0996d401f115e",]

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

     resource "aws_network_acl" "acl-c31fc4a4" {
        vpc_id = "vpc-4a50ae2d"
        subnet_ids = ["subnet-35d6d","subnet-09a005","subnet-bdb380",]

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

    PYTHONPATH=. python utils2devops/aws/network_acl.py

    resource "aws_network_acl" "acl-0682c7" {
        vpc_id = "vpc-0b24bc90e75638"
        subnet_ids = ["subnet-061f115e",]

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

     resource "aws_network_acl" "acl-c31fc4" {
        vpc_id = "vpc-4a50ae2d"
        subnet_ids = ["subnet-35d6d","subnet-09a730","subnet-bb380","subnet-a35833c6","subnet-e392f0c9","subnet-ad0e52db",]

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
