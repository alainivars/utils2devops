# Update minimum this with  your AWS config
variable "vpc_id" {
  description = "Vpc Id where to deploy the node of the simple swarm"
  default     = "vpc-4a50ae2d"
}

variable "subnet_id" {
  description = "Subnet in the Vpc Id where to deploy the node of the simple swarm"
  default     = "subnet-09a73005"
}

variable "aws_region" {
  description = "AWS region on which we will setup the swarm cluster"
  default     = "us-east-1"
}

variable "key_name" {
  description = "Desired name of Keypair..."
  default     = "terraform_key"  #OK "terraform_ec2_key"
}

# You could change these but they default values are good fot that test
variable "instance_count" {
  description = "Number of instances to launch"
  type        = number
  default     = 5
}

variable "name" {
  description = "Name to be used on all resources as prefix"
  type        = string
  default     = "swarm-node"
}

variable "instance_type" {
  description = "Instance type"
  default     = "t2.micro"
}

variable "ssh_user" {
  description = "ssh user, depent on the distrubution instaled"
  default     = "ubuntu"
}
