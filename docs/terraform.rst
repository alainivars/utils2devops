
.. include:: links.inc

To use terraform_import and aws
###############################

require::

    sudo pip3 install --upgrade awscli
    export PATH=/home/ec2-user/.local/bin:$PATH

Create an AWS account (it's free)::

    https://aws.amazon.com/


Install Terraform::

    https://learn.hashicorp.com/terraform/getting-started/install.html



To test it
##########
create a main.tf and add this inside::

    provider "aws" {
      region = "us-east-2"
    }

    resource "aws_lambda_function" "lambda" {
        # (resource arguments)
    }

    resource "aws_s3_bucket" "bucket" {
        # (resource arguments)
    }

log on your AWS account, and create::

    - an s3 bucket named my-bucket-test-1
    - a lambda function my-lambda-test-1

then import them by::

    terraform import aws_lambda_function.lambda my-lambda-test-1

    terraform import aws_s3_bucket.bucket my-bucket-test-1

    terraform import aws_network_acl.main acl-f1780b98

    terraform import aws_lambda_layer_version.test_layer arn:aws:lambda:us-east-2:397270606208:layer:aws_lambda_read_s3:1


Then a terraform.tfstate will be generated or updated with your config.TODO the documentation of existing functionnalities
TODO implementation WORK IN PROGESS
