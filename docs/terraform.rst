
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

Generate a Key pair for terraform user::

    cd ~/.ssh
    ssh-keygen -f terraform_key
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in terraform_key.
    Your public key has been saved in terraform_key.pub.
    The key fingerprint is:
    SHA256:SX5+SVVbyUiaslXmpqFNJl8WrP/NMTzWMnsK5AwxMvI alain@Beowolf007
    The key's randomart image is:
    +---[RSA 2048]----+
    |            o=o +|
    |            *o.+o|
    |      . +ooB.=.. |
    |       = +@+*.   |
    |        Eoo++ . .|
    |         o * oo*.|
    |          . * o==|
    |           . ...+|
    |              .o |
    +----[SHA256]-----+

We now have 2 more files::

    terraform_key
    terraform_key.pub

Creating the terraform file to import it::
See :ref:`ref-create-dm` for setting your profile

    provider "aws" {
      profile = "terraform"
      region  = "eu-west-1"
    }

    resource "aws_instance" "ubuntu_zesty" {
      ami           = "ami-6b7f610f"
      instance_type = "t2.micro"
      key_name      = "terraform_ec2_key"
    }

    resource "aws_key_pair" "terraform_ec2_key" {
      key_name = "terraform_ec2_key"
      public_key = "${file("terraform_key.pub")}"
//      public_key = "ssh-rsa AZEB...jkasASDhaSjdh me@here"
    }

