# inspirated by:
# https://github.com/rsmitty/cross-cloud-swarm/blob/master/02-create-inv.tf

resource "null_resource" "ansible-provision" {
  depends_on = ["module.swarm_cluster"] //, "aws_instance.aws-swarm-members", "google_compute_instance.gce-swarm-members"]

  provisioner "local-exec" {
    command = "echo \"[swarm_master]\" > swarm-inventory"
  }

  provisioner "local-exec" {
    command = "echo \"${format("%s ansible_ssh_user=%s", module.swarm_cluster_manager.public_ip[0], var.ssh_user)}\" >> swarm-inventory"
  }

  provisioner "local-exec" {
    command = "echo \"\n[swarm_managers]\" >> swarm-inventory"
  }

  provisioner "local-exec" {
    command = "echo \"${format("%s ansible_ssh_user=%s", module.swarm_cluster_manager.public_ip, var.ssh_user)}\" >> swarm-inventory"
  }

  provisioner "local-exec" {
    command = "echo \"\n[swarm_nodes]\" >> swarm-inventory"
  }

  provisioner "local-exec" {
    command = "echo \"${join("\n",formatlist("%s ansible_ssh_user=%s", module.swarm_cluster_worker.public_ip, var.ssh_user))}\" >> swarm-inventory"
  }

  provisioner "local-exec" {
    command = "echo \"\n\n# Aws Swarm config\n${join("\n",formatlist("Host %s\n\tHostname %s\n\tUser %s\n\tIdentityFile ~/.ssh/terraform_key\n", module.swarm_cluster_manager.public_ip, module.swarm_cluster_manager.public_ip, var.ssh_user))}\" >> ~/.ssh/config"
  }

  provisioner "local-exec" {
    command = "echo \"${join("\n",formatlist("Host %s\n\tHostname %s\n\tUser %s\n\tIdentityFile ~/.ssh/%s\n", module.swarm_cluster_worker.tags[*]["Name"], module.swarm_cluster_worker.public_ip, var.ssh_user, var.key_name))}\" >> ~/.ssh/config"
  }
}
