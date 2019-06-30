
.. include:: links.inc


Swarm Stack local-simple
========================
Before using these make sure you had clone the repository by::

    git submodule update --init --recursive

Now let's go..

(*) All Open Sources
+--------------------+-----------------------------+
| Services           | Software                    |
+====================+=============================+
| GUI Control        | `Portainer`_                   |
+--------------------+-----------------------------+
| Central Monitoring | Promotheus + Grafana        |
+--------------------+-----------------------------+
| Central Logging    | Elastic ELK                 |
+--------------------+-----------------------------+
| Layer 7 Proxy      |                             |
+--------------------+-----------------------------+
| Storage            | Local File System           |
+--------------------+-----------------------------+
| Networking         | Docker Swarm Overlay        |
+--------------------+-----------------------------+
| Orchestration      | Docker Swarm                |
+--------------------+-----------------------------+
| Runtime            | Docker CE                   |
+--------------------+-----------------------------+
| Machine and OS     | Docker Machine + VirtualBox |
+--------------------+-----------------------------+

1/ Create the Machine::

    ./utils2devops/bin/docker-machine-cluster.sh -c 5

| You can go to see the doc of this tools here :ref:`ref-create-dm`
| Here we will create a swarm with 3 machines

2/ Enable monitoring (optional)::

    ./utils2devops/bin/enable-monitoring.sh -p ./utils2devops/docker/ -n 5

3/ Create the Docker Swarm::

    ./utils2devops/bin/swarm.sh -c -m 3 -w 2

| You can go to see the doc of this tools here :ref:`ref-create-sw`
| Here we will create a swarm with 3 manager and 2 worker

4/ To launch docker command in the Master with ssh it::

    eval "$(docker-machine env node-1)"

5/ Deploy Ops Stacks Graphics UI (optional)::

    docker stack deploy -c ./utils2devops/docker/local-simple/portainer.yml portainer
    or the very light
    docker stack deploy -c ./utils2devops/docker/local-simple/visualizer/visualizer.yml visualizer

| After these steps we will have a Portainer at:
| http://<ip-node-1>:9000/#/dashboard
| http://<ip-node-1>:9000/#/containers
| http://<ip-node-1>:9000/#/swarm/visualizer
| and so many other... have a look here https://www.portainer.io/overview/

6/ Deploy Ops Stacks::

    docker stack deploy -c ./submodules/swarmprom/docker-compose.yml prom
    docker stack deploy -c ./utils2devops/docker/local-simple/elk.yml elk

| After these steps we will have a Grafana Swarm nodes at:
| http://<ip-node-1>:3000/d/BPlb-Sgik/docker-swarm-nodes?refresh=30s&orgId=1
| After these steps we will have a Grafana Swarm Services at:
| http://<ip-node-1>:3000/d/zr_baSRmk/docker-swarm-services?refresh=30s&orgId=1
| After these steps we will have a Promotheus Stat at:
| http://<ip-node-1>:3000/d/mGFfYSRiz/prometheus-2-0-stats?refresh=1m&orgId=1
| After these steps we will have a Promotheus Query at:
| http://<ip-node-1>::9090/graph
| After these steps we will have a Alert manager at:
| http://<ip-node-1>:9093/#/alerts
| After these steps we will have a Alert Dashboard at:
| http://<ip-node-1>:9094/?q=
| After these steps we will have a Elasticsearch at:
| http://<ip-node-1>:9200
| After these steps we will have a kibana at:
| http://<ip-node-1>:5601/app/kibana#/management/kibana/index?_g=()

Swarm Stack local
=================
WORK IN PROGRESS
Before using these make sure you had clone the repository by::

    git submodule update --init --recursive

That example of local deployment is nearly the same to the previews one
except we will ad the reverse proxy Traefik to permit to us to have many
more service even if they need the same port!
| Even if in surface that llok like same, the deployment file are all
modified!
| Now let's go..

(*) All Open Sources
+--------------------+-----------------------------+
| Services           | Software                    |
+====================+=============================+
| GUI Control        | `Portainer`_                   |
+--------------------+-----------------------------+
| Central Monitoring | Promotheus + Grafana        |
+--------------------+-----------------------------+
| Central Logging    | Elastic ELK                 |
+--------------------+-----------------------------+
| Layer 7 Proxy      | `Traefik`_                     |
+--------------------+-----------------------------+
| Storage            | Local File System           |
+--------------------+-----------------------------+
| Networking         | Docker Swarm Overlay        |
+--------------------+-----------------------------+
| Orchestration      | Docker Swarm                |
+--------------------+-----------------------------+
| Runtime            | Docker CE                   |
+--------------------+-----------------------------+
| Machine and OS     | Docker Machine + VirtualBox |
+--------------------+-----------------------------+

1/ Create the Machine::

    ./utils2devops/bin/docker-machine-cluster.sh -c 5

| You can go to see the doc of this tools here :ref:`ref-create-dm`
| Here we will create a swarm with 3 machines

2/ Enable monitoring (optional)::

    ./utils2devops/bin/enable-monitoring.sh -p ./utils2devops/docker/ -n 5

3/ Create the Docker Swarm::

    ./utils2devops/bin/swarm.sh -c -m 3 -w 2

| You can go to see the doc of this tools here :ref:`ref-create-sw`
| Here we will create a swarm with 3 manager and 2 worker

4/ To launch docker command in the Master with ssh it::

    eval "$(docker-machine env node-1)"

5/ Deploy Traefik::

    docker stack deploy -c ./utils2devops/docker/local/traefik.yml traefik

| After this step we will have a proxy Dashboard at:
| http://<ip-node-1>:8080/dashboard/

7/ Deploy Ops Stacks::

    docker stack deploy -c ./utils2devops/docker/local/swarmprom.yml prom
    docker stack deploy -c ./utils2devops/docker/local/elk.yml elk
    docker stack deploy -c ./utils2devops/docker/local/portainer.yml portainer
    docker stack deploy -c ./utils2devops/docker/local/visualizer/visualizer.yml visualizer

| After these steps we will have a Dashboard at:
| http://<ip-node-1>:8080/dashboard/


Simple Swarm Stack AWS
======================
# TODO
(*) All Open Sources
+--------------------+-----------------------------+
| Services           | Software                    |
+====================+=============================+
| GUI Control        | `Portainer`_                   |
+--------------------+-----------------------------+
| Central Monitoring | Promotheus + Grafana        |
+--------------------+-----------------------------+
| Central Logging    | Elastic ELK                 |
+--------------------+-----------------------------+
| Layer 7 Proxy      | `Traefik`_ + Let's Encrypt     |
+--------------------+-----------------------------+
| Storage            | REX-Ray                     |
+--------------------+-----------------------------+
| Networking         | Docker Swarm Overlay        |
+--------------------+-----------------------------+
| Orchestration      | Docker Swarm                |
+--------------------+-----------------------------+
| Runtime            | Docker CE                   |
+--------------------+-----------------------------+
| Machine and OS     | Docker Machine + VirtualBox |
+--------------------+-----------------------------+


1/ Create the Machine::

    ./utils2devops/bin/docker-machine-cluster.sh -c 5

| You can go to see the doc of this tools here :ref:`ref-create-dm`
| Here we will create a swarm with 3 machines

2/ Enable monitoring (optional)::

    ./utils2devops/bin/enable-monitoring.sh -p ./utils2devops/docker/ -n 5


3/ Create the Docker Swarm::

    ./utils2devops/bin/swarm.sh -c -m 3 -w 2

| You can go to see the doc of this tools here :ref:`ref-create-sw`
| Here we will create a swarm with 3 manager and 2 worker

4/ To launch docker command in the Master with ssh it::

    eval "$(docker-machine env node-1)"

5/ Deploy RexRay plug-in:: DON'T WORK ACTUALLY !!!

    docker stack deploy -c ./utils2devops/docker/stack-rexray.yml rexray
| you can see here if you want really install it
| https://github.com/rexray/rexray/issues/1194
| https://github.com/thecodeteam/labs/tree/master/setup-virtualbox-dockermachine
| https://stackoverflow.com/questions/41387121/unable-to-mount-persistent-volume-to-docker-container-using-rex-ray-and-virtualb
| https://github.com/rexray/rexray/blob/02e0154f7b41dc6e56bf8b0ec2a131edef115c07/.docs/user-guide/storage-providers/virtualbox.md
| https://github.com/rexray/rexray/blob/master/Vagrantfile

6/ Deploy Traefik with Let's Encrypt::

    docker stack deploy -c ./utils2devops/docker/local/traefik.yml traefik

| After this step we will have a proxy Dashboard at:
| http://<ip-node-1>:8080/dashboard/

7/ Deploy Ops Stacks::

    docker stack deploy -c ./utils2devops/docker/stack-swarmprom.yml prom
    docker stack deploy -c ./utils2devops/docker/stack-elk.yml elk
    docker stack deploy -c ./utils2devops/docker/stack-portainer.yml portainer

| After these steps we will have a Dashboard at:
| http://<ip-node-1>:8080/dashboard/

