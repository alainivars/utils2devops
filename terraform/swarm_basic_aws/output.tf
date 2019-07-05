output "image_id" {
    value = data.aws_ami.ubuntu.id
}

output "key_name" {
  value       = var.key_name
  description = "The key name to access to the nodes instance."
}

# master and manager
output "ids_manager" {
  description = "List of IDs of instances"
  value       = module.swarm_cluster_manager.id
}

output "name_manager" {
  description = "List of public Names assigned to the instances manager"
  value       = module.swarm_cluster_manager.tags[*]["Name"]
}

output "public_dns_manager" {
  description = "List of public DNS names assigned to the instances manager"
  value       = module.swarm_cluster_manager.public_dns
}

output "public_ip_manager" {
  description = "List of public DNS names assigned to the instances manager"
  value       = module.swarm_cluster_manager.public_ip
}

output "vpc_security_group_ids_manager" {
  description = "List of VPC security group ids assigned to the instances manager"
  value       = module.swarm_cluster_manager.vpc_security_group_ids
}

output "instance_id_manager" {
  description = "EC2 instance ID manager"
  value       = module.swarm_cluster_manager.id[0]
}

output "instance_public_dns_manager" {
  description = "Public DNS name assigned to the EC2 instance manager"
  value       = module.swarm_cluster_manager.public_dns[0]
}

# worker
output "ids_worker" {
  description = "List of IDs of instances worker"
  value       = module.swarm_cluster_worker.id
}

output "name_worker" {
  description = "List of public Names assigned to the instances worker"
  value       = module.swarm_cluster_worker.tags[*]["Name"]
}

output "public_dns_worker" {
  description = "List of public DNS names assigned to the instances worker"
  value       = module.swarm_cluster_worker.public_dns
}

output "public_ip_worker" {
  description = "List of public DNS names assigned to the instances worker"
  value       = module.swarm_cluster_worker.public_ip
}

output "vpc_security_group_ids_worker" {
  description = "List of VPC security group ids assigned to the instances worker"
  value       = module.swarm_cluster_worker.vpc_security_group_ids
}

output "instance_id_worker" {
  description = "EC2 instance ID worker"
  value       = module.swarm_cluster_worker.id[0]
}

output "instance_public_dns_worker" {
  description = "Public DNS name assigned to the EC2 instance worker"
  value       = module.swarm_cluster_worker.public_dns[0]
}
