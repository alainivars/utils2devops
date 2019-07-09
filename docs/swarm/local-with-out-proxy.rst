
.. include:: ../links.inc


Swarm Stack local-with-out-proxy
================================
Before using these make sure you had clone the repository by::

    git submodule update --init --recursive

Now let's go..

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

You have 2 way to deploy it::

    - The fast way by launch the ansible workbook, just type:

        ansible-playbook -i ansible/swarm/local-inventory ansible/swarm/local-with-out-proxy.yml
        # NOTE: that will take around 5 minutes

    - Or the long way but where you can learn every step ...

Learn every step to deploy the swarm local-with-out-proxy
---------------------------------------------------------

1/ Create the Machine::

    ./utils2devops/bin/docker-machine-cluster.sh -c 5

| You can go to see the doc of this tools here :ref:`ref-create-docker_machine`
| Here we will create a swarm with 5 machines

2/ Enable monitoring (optional)::

    ./utils2devops/bin/enable-monitoring.sh -p ./utils2devops/docker/ -n 5

3/ Create the Docker Swarm::

    ./utils2devops/bin/swarm.sh -c -m 3 -w 2

| You can go to see the doc of this tools here :ref:`ref-create-sw`
| Here we will create a swarm with 3 manager and 2 worker

4/ Launch docker command in the Master::

    eval "$(docker-machine env node-1)"

5/ Deploy Ops Stacks Graphics UI (optional)::

    export PORTAINER_HOST=portainer.example.com
    docker stack deploy -c ./utils2devops/docker/local-with-out-proxy/portainer.yml portainer

After these steps we will have a Portainer at::

    Portainer at:
        http://<ip-node-1>:9000/#/init/admin
        http://<ip-node-1>:9000/#/dashboard
        http://<ip-node-1>:9000/#/containers
        http://<ip-node-1>:9000/#/swarm/visualizer
    and so many other... have a look here https://www.portainer.io/overview/

6/ Deploy Ops Stacks::

    docker stack deploy -c ./submodules/swarmprom/docker-compose.yml prom
    docker stack deploy -c ./utils2devops/docker/local-with-out-proxy/elk.yml elk

After these steps we will have ::

    Grafana login at:
        https://<ip-node-1>/login
    Grafana Swarm nodes at:
        https://<ip-node-1>:3000/d/BPlb-Sgik/docker-swarm-nodes?refresh=30s&orgId=1
    Grafana Swarm Services at:
        https://<ip-node-1>:3000/d/zr_baSRmk/docker-swarm-services?refresh=30s&orgId=1
    Promotheus Stat at:
        http://<ip-node-1>:3000/d/mGFfYSRiz/prometheus-2-0-stats?refresh=1m&orgId=1
    Promotheus Query at::
        https://<ip-node-1>::9090/graph
    Alert manager at:
        https://<ip-node-1>:9093/#/alerts
    Alert Dashboard at:
        https://<ip-node-1>:9094/?q=
    Elasticsearch at:
        http://elasticsearch.example.com/
    kibana at:
        http://kibana.example.com/app/kibana#/home?_g=()
    and much more have a look at https://github.com/stefanprodan/swarmprom

Now it's ready to deploy your apps and test them::

    docker stack deploy my_company/my_services my_service

When you have finish to use it, Destroy it by::

    ./utils2devops/bin/docker-machine-cluster.sh -d 5
