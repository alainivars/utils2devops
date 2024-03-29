
.. include:: ../links.inc

Swarm Stack local-proxy-prom-Icinga2
====================================

Before using these make sure you had clone the repository by::

    git submodule update --init --recursive

That example of local deployment is nearly the same to the previews one
except we will replace ELK by Icinga2 + plugin logs!
| Now let's go..

(*) All Open Sources

+--------------------+-----------------------------+
| Services           | Software                    |
+====================+=============================+
| GUI Control        | `Portainer`_                |
+--------------------+-----------------------------+
| Central Monitoring | Promotheus + Grafana        |
+--------------------+-----------------------------+
| Central Logging    | Icinga2                     |
+--------------------+-----------------------------+
| Layer 7 Proxy      | `Traefik`_                  |
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

        ansible-playbook -i ansible/swarm/local-inventory ansible/swarm/local-proxy-prom-icinga2.yml
        # NOTE: that will take around 5 minutes

    - Or the long way but where you can learn every step ...

Deployment step by step
-----------------------

1/ Create the Machine::

    ./utils2devops/bin/docker-machine-cluster.sh -c 5

| You can go to see the doc of this tools here :ref:`ref-create-docker_machine`
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

    export TRAEFIK_HOST=traefik.yourdomain
    default value: traefik.example.com
    export TRAEFIK_PUBLIC_TAG=my-traefik-public
    default value: traefik-public
    docker stack deploy -c ./utils2devops/docker/local-proxy-prom-icinga2/traefik.yml traefik

After this step we will have a proxy Dashboard at::

    http://traefik.example.com:8080/dashboard/

7/ Deploy Ops Stacks Graphics UI (optional)::

    export PORTAINER_HOST=portainer.yourdomain
    default value: portainer.example.com
    docker stack deploy -c ./utils2devops/docker/local-with-prom-elk/portainer.yml portainer

After these steps we will have::

    Portainer at:
        http://portainer.example.com/#/init/admin
        http://portainer.example.com/#/dashboard
        http://portainer.example.com/#/containers
        http://portainer.example.com/#/swarm/visualizer
    and so many other... have a look here https://www.portainer.io/overview/

8/ Deploy Ops Stacks::

    export ADMIN_USER=admin
    default value: admin
    export ADMIN_PASSWORD=adminadmin
    default value: adminadmin
    export HASHED_PASSWORD=$(openssl passwd -apr1 -salt pepper $ADMIN_PASSWORD)

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
    export SLACK_CHANNEL=utils2devops-tests
    default value: general
    export SLACK_USER=alertmanager
    default value: alertmanager

Then we continue to deploy with swarmprom::

    docker stack deploy -c ./utils2devops/docker/local-proxy-prom-icinga2/swarmprom.yml prom


After these steps we will have ::

    Grafana login at:
        https://grafana.example.com/login
    Grafana Swarm nodes at:
        https://grafana.example.com/d/BPlb-Sgik/docker-swarm-nodes?refresh=30s&orgId=1
    Grafana Swarm Services at:
        https://grafana.example.com/d/zr_baSRmk/docker-swarm-services?refresh=30s&orgId=1
    Promotheus Stat at:
        http://grafana.example.com/d/mGFfYSRiz/prometheus-2-0-stats?refresh=1m&orgId=1
    Promotheus Query at::
        https://prometheus.example.com/graph
    Alert manager at:
        https://alertmanager.example.com/#/alerts
    Alert Dashboard at:
        https://unsee.example.com/?q=

In promotheus try::

    sum(irate(container_cpu_usage_seconds_total{image!=""}[1m])) without (cpu)
    container_memory_usage_bytes{image!=""}
    sum(rate(container_network_transmit_bytes_total{image!=""}[1m])) without (interface)
    sum(rate(container_fs_reads_bytes_total{image!=""}[1m])) without (device)
    sum(rate(container_fs_writes_bytes_total{image!=""}[1m])) without (device)

Then we finish to deploy with elk::

    export ELASTICSEARCH_USER=admin
    default value: admin
    export ELASTICSEARCH_PASSWORD=adminadmin
    default value: admin
    export ELASTICSEARCH_HASHED_PASSWORD=$(openssl passwd -apr1 -salt pepper $ELASTICSEARCH_PASSWORD)
    export KIBANA_USER=admin
    default value: admin
    export KIBANA_PASSWORD=adminadmin
    default value: admin
    export KIBANA_HASHED_PASSWORD=$(openssl passwd -apr1 $KIBANA_PASSWORD)
    docker stack deploy -c ./utils2devops/docker/local-proxy-prom-icinga2/elk.yml elk


After these steps we will have::

    Elasticsearch at:
        http://elasticsearch.example.com/
    kibana at:
        http://kibana.example.com/app/kibana#/home?_g=()
    and much more have a look at https://github.com/stefanprodan/swarmprom

Note:
| To use elasticsearch you will have to increase the max virtual memory or you will get:
| WARN: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
| It can be fixed by running on the node:
| sysctl -w vm.max_map_count=262144 in terminal (Linux/Ubuntu).
| Or permanently by create a file name 60-elasticsearch.conf and place it in /etc/sysctl.d/ with the following content:
| vm.max_map_count=262144

Now it's ready to deploy your apps and test them::

    docker stack deploy my_company/my_services my_service

When you have finish to use it, Destroy it by::

    ./utils2devops/bin/docker-machine-cluster.sh -d 5


