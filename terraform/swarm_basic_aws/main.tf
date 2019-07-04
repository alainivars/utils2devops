# Specify the provider and access details
provider "aws" {
  version = "~> 2.0"
//  access_key = "your-aws-access-key"
//  secret_key = "your-aws-secret-access-key"
  profile = "terraform"
  region = var.aws_region
}

//resource "aws_key_pair" "terraform_ec2_key_pair" {
//  key_name = var.key_name
//  public_key = "${file(var.public_key_file)}"
//}

data "aws_ami" "ubuntu" {
    most_recent = true

    filter {
        name   = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*"]
    }

    filter {
        name   = "virtualization-type"
        values = ["hvm"]
    }

    owners = ["099720109477"] # Canonical
}

resource "aws_security_group" "swarm-security-group" {
  name        = "swarm-security-group"
  description = "Swarm security group to allow inbound/outbound from the VPC"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "SSH traffic"
  }

  ingress {
    from_port   = 2376
    to_port     = 2376
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Docker Machine Orchestrate"
  }

  ingress {
    from_port   = 2377
    to_port     = 2377
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Docker Swarm comm. between nodes"
  }

  ingress {
    from_port   = 4789
    to_port     = 4789
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Docker Swarm overlay network"
  }

  ingress {
    from_port   = 7946
    to_port     = 7946
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "TCP Docker Swarm container network discovery"
  }

  ingress {
    from_port   = 7946
    to_port     = 7946
    protocol    = "udp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "UDP Docker Swarm container network discovery"
  }

  ingress {
    from_port = 8
    to_port = 0
    protocol = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Ping"
  }

  egress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "swarm-security-group"
  }
}

module "swarm_cluster" {
  source                 = "terraform-aws-modules/ec2-instance/aws"
  version                = "~> 2.0"

  name                   = var.name
  instance_count         = var.instance_count

  associate_public_ip_address = true

  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_type
  key_name               = var.key_name
  monitoring             = false
  vpc_security_group_ids = [aws_security_group.swarm-security-group.id]
  subnet_id              = var.subnet_id

  tags = {
    Terraform   = "true"
  }
}
