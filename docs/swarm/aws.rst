
.. include:: ../links.inc

Swarm Stack AWS
===============
WORK IN PROGRESS
Before using these make sure you had clone the repository by::

    git submodule update --init --recursive

For working in the cloud I strongly recommend to you to create a key for each
provider, if you don't already have a key for Aws, you create it by::

    ssh-keygen -t rsa -b 4096 -C your@email.address
    At the prompt name it with aws in the name (but it's up to you)

That example of local deployment is nearly the same to the previews one
except we will ad the reverse proxy Traefik to permit to us to have many
more service even if they need the same port!
| Now let's go..

(*) All Open Sources

+--------------------+-----------------------------+
| Services           | Software                    |
+====================+=============================+
| GUI Control        | `Portainer`_                |
+--------------------+-----------------------------+
| Central Monitoring | Promotheus + Grafana        |
+--------------------+-----------------------------+
| Central Logging    | Elastic ELK                 |
+--------------------+-----------------------------+
| Layer 7 Proxy      | `Traefik`_                  |
+--------------------+-----------------------------+
| Storage            | AWS S3, RDS, Elasticsearch  |
+--------------------+-----------------------------+
| Networking         | Docker Swarm Overlay        |
+--------------------+-----------------------------+
| Orchestration      | Docker Swarm                |
+--------------------+-----------------------------+
| Runtime            | Docker CE                   |
+--------------------+-----------------------------+
| Machine and OS     | AWS EC2                     |
+--------------------+-----------------------------+

1/ Setup the configuration:

Go in the work directory::

    cd terraform/swarm_basic_aws

Edit the terraform file configuration file variable.tf::

    variable "aws_region" {
      description = "AWS region on which we will setup the swarm cluster"
      default     = "us-east-1" <= Here change it to Aws of your VPC
    }

    variable "vpc_id" {
      description = "Vpc Id where to deploy the node of the simple swarm"
      default     = "vpc-4a50ae2d" <= Here change it to your Aws VPC
    }

    variable "subnet_id" {
      description = "Subnet in the Vpc Id where to deploy the node of the simple swarm"
      default     = "subnet-09a73005" <= Here change it to your Aws subnet
    }

    variable "key_name" {
      description = "Desired name of Keypair..."
      default     = "terraform_ec2_key" <= Here change it to your Aws key pair
    }

2/ Create the Nodes on Aws::

    terraform init
    terraform plan
    terraform apply

The ec2 instances are created and added at the end of your ~/.ssh/config::

    # Aws Swarm config
    Host 18.207.251.225
        Hostname 18.207.251.225
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

    Host 18.205.176.71
        Hostname 18.205.176.71
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

    Host 18.205.66.206
        Hostname 18.205.66.206
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

    Host 18.232.31.117
        Hostname 18.232.31.117
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

    Host 18.232.188.237
        Hostname 18.232.188.237
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

    Host swarm-node-1
        Hostname 18.207.251.225
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

    Host swarm-node-2
        Hostname 18.205.176.71
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

    Host swarm-node-3
        Hostname 18.205.66.206
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

    Host swarm-node-4
        Hostname 18.232.31.117
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

    Host swarm-node-5
        Hostname 18.232.188.237
        User ubuntu
        IdentityFile ~/.ssh/terraform_key

| The ones with "Host <IP>" are Ansible need it.
| The ones with "Host node-x" are you in case you want SSH to.

Edit the file swarm-inventory and remove the first line of [swarm_nodes]::

    [swarm_master]
    18.207.251.225 ansible_ssh_user=ubuntu

    [swarm_manager]

    [swarm_nodes]
    18.207.251.225 ansible_ssh_user=ubuntu <= Here delete that line, it a duplicate!
    18.205.176.71 ansible_ssh_user=ubuntu
    18.205.66.206 ansible_ssh_user=ubuntu
    18.232.31.117 ansible_ssh_user=ubuntu
    18.232.188.237 ansible_ssh_user=ubuntu

| It's a bug and I'm looking how to fix it, any advice ?
| TODO: fix the problem in file create_inventory.tf line 20

IMPORTANT: It's here you can choice Which one is manager and how many, you can by example set 3 manager and 2 worker, like that::

    [swarm_master]
    18.207.251.225 ansible_ssh_user=ubuntu

    [swarm_manager]
    18.205.176.71 ansible_ssh_user=ubuntu
    18.205.66.206 ansible_ssh_user=ubuntu

    [swarm_nodes]
    18.232.31.117 ansible_ssh_user=ubuntu
    18.232.188.237 ansible_ssh_user=ubuntu

3/ Create the Docker Swarm::

    ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -b -i swarm-inventory swarm.yml

Now the swarm is deployed and ready to use on all the swarm-node-x

4/ Add node-1 in docker-machine to launch docker command in the Master from local::

    docker-machine create \
      --driver generic \
      --generic-ssh-user "ubuntu" \
      --generic-ip-address=35.170.64.155 \
      --generic-ssh-key ~/.ssh/terraform_key \
      swarm-node-1

    eval "$(docker-machine env swarm-node-1)"

5/ Deploy Traefik::

    export TRAEFIK_HOST=traefik.cloud.my
    default value: traefik.cloud.my
    export TRAEFIK_PUBLIC_TAG=my-traefik-public
    default value: traefik-public
    docker stack deploy -c ../../utils2devops/docker/cloud-simple/traefik.yml traefik

After this step we will have a proxy Dashboard at::

    http://traefik.cloud.my:8080/dashboard/

7/ Deploy Ops Stacks Graphics UI (optional)::

    export PORTAINER_HOST=portainer.cloud.my
    default value: portainer.example.com
    docker stack deploy -c ../../utils2devops/docker/cloud-simple/portainer.yml portainer

After these steps we will have::

    Portainer at:
        http://portainer.example.com:9000/#/init/admin
        http://portainer.example.com:9000/#/dashboard
        http://portainer.example.com:9000/#/containers
        http://portainer.example.com/#/swarm/visualizer
    and so many other... have a look here https://www.portainer.io/overview/

8/ Deploy Ops Stacks::

    export ADMIN_USER=admin
    default value: admin
    export ADMIN_PASSWORD=adminadmin
    default value: adminadmin
    export HASHED_PASSWORD=$(openssl passwd -apr1 $ADMIN_PASSWORD)

You can check the contents with::

    echo $HASHED_PASSWORD

it will look like::

    $apr1$TsqS2JR3$oGG0NFZsU1VdKn03MAyjh.

Create and export an environment variable DOMAIN, e.g.:::

    export DOMAIN=example.com

and make sure that the following sub-domains point to your Docker Swarm cluster IPs::

    grafana.example.com
    alertmanager.example.com
    unsee.example.com
    prometheus.example.com

Note: You can also use a subdomain, like swarmprom.example.com. Just make sure that the
subdomains point to (at least one of) your cluster IPs. Or set up a wildcard subdomain (*).

Set and export an environment variable with the tag used by Traefik public to filter services (by default, it's traefik-public)::

    export TRAEFIK_PUBLIC_TAG=traefik-public

If you are using Slack and want to integrate it, set the following environment variables::

    export SLACK_URL=https://hooks.slack.com/services/TOKEN
    default value: https://hooks.slack.com/services/TOKEN
    export SLACK_CHANNEL=devops-alerts
    default value: general
    export SLACK_USER=alertmanager
    default value: alertmanager

Then we continue to deploy with swarmprom::

    docker stack deploy -c ./utils2devops/docker/cloud/aws/swarmprom.yml prom


After these steps we will have ::

    Grafana Swarm nodes at:
        https://grafana.example.com/d/BPlb-Sgik/docker-swarm-nodes?refresh=30s&orgId=1
    Grafana Swarm Services at:
        https://grafana.example.com/d/zr_baSRmk/docker-swarm-services?refresh=30s&orgId=1
    Promotheus Stat at:
        http://<ip-node-1>:3000/d/mGFfYSRiz/prometheus-2-0-stats?refresh=1m&orgId=1
    Promotheus Query at::
        https://prometheus.example.com/graph
    Promotheus Status targets:
        https://prometheus.example.com/targets
    Alert manager at:
        https://alertmanager.example.com/#/alerts
    Alert Dashboard at:
        https://unsee.example.com/?q=

Then we finish to deploy with elk::

    export ELASTICSEARCH_USER=admin
    default value: admin
    export ELASTICSEARCH_PASSWORD=adminadmin
    default value: admin
    export ELASTICSEARCH_HASHED_PASSWORD=$(openssl passwd -apr1 $ELASTICSEARCH_PASSWORD)
    export KIBANA_USER=admin
    default value: admin
    export KIBANA_PASSWORD=adminadmin
    default value: admin
    export KIBANA_HASHED_PASSWORD=$(openssl passwd -apr1 $KIBANA_PASSWORD)
    docker stack deploy -c ./utils2devops/docker/cloud/aws/elk.yml elk


After these steps we will have::

    Elasticsearch at:
        http://elasticsearch.example.com/
    kibana at:
        http://kibana.example.com/app/kibana#/home?_g=()
    and much more have a look at https://github.com/stefanprodan/swarmprom

Now it's ready to deploy your apps and test them::

    docker stack deploy my_company/my_services my_service

When you have finish to use it, Destroy it by::

    terraform destroy
    docker-machine rm node-1

    Remove all the entries added at the end of your ~/.ssh/config, all from "# Aws Swarm config"::

        # Aws Swarm config
        Host *

