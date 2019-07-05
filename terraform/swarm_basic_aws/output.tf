output "image_id" {
    value = data.aws_ami.ubuntu.id
}

output "key_name" {
  value       = var.key_name
  description = "The key name to acces to the nodes instance."
}

output "ids" {
  description = "List of IDs of instances"
  value       = module.swarm_cluster.id
}

output "name" {
  description = "List of public Names assigned to the instances"
  value       = module.swarm_cluster.tags[*]["Name"]
}

output "public_dns" {
  description = "List of public DNS names assigned to the instances"
  value       = module.swarm_cluster.public_dns
}

output "public_ip" {
  description = "List of public DNS names assigned to the instances"
  value       = module.swarm_cluster.public_ip
}

output "vpc_security_group_ids" {
  description = "List of VPC security group ids assigned to the instances"
  value       = module.swarm_cluster.vpc_security_group_ids
}

output "instance_id" {
  description = "EC2 instance ID"
  value       = module.swarm_cluster.id[0]
}

output "instance_public_dns" {
  description = "Public DNS name assigned to the EC2 instance"
  value       = module.swarm_cluster.public_dns[0]
}
