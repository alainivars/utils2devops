
.. include:: links.inc

.. _ref-create-dm:
Create your local cluster of docker-machine
###########################################

This script will create x nodes docker-machine named node-1 to name-n,
the purpose of this script is for local debug or tests, you can after
access to these by::

    docker-machine ssh node-n


required::

    install Docker-machine:
    https://docs.docker.com/machine/install-machine/

run::

    ./utils2devops/bin/docker-machine-cluster.sh
    started...
    usage:
      docker-machine-cluster [-h | --help] To get this help
      docker-machine-cluster [-c | --create x]
          Where x is the number of manager node to create/add in the swarm.
      docker-machine-cluster [-d | --destroy x]
          Where x is the number of manager node to create/add in the swarm.

Create a cluster of 4 node::

    ./utils2devops/bin/docker-machine-cluster.sh -c 5

Destroy it::

    ./utils2devops/bin/docker-machine-cluster.sh -d 5


.. _ref-create-sw:
Create a Docker Swarm on nodes docker-machine
#############################################

This script will create a swarm on nodes docker-machine named node-1 to name-n,
the purpose of this script is for local debug or tests, you can after
access to these by::

    docker-machine ssh node-n


required::

    install Docker Swarm:
    https://docs.docker.com/engine/swarm/

run::

    ./utils2devops/bin/swarm.sh
    started...
    usage:
      swarm [-h | --help] To get this help
          If the docker-swarm don't exist it will be created
      swarm -c|--create [-m|--count_manager x -w|--count_worker y] To create node to a swarm
          Where x is the number of manager node to create/add in the swarm.
          Where y is the number of worker node to create/add in the swarm.
      swarm -r|--remove x] To destroy a swarm
          Where x is the number of node in the swarm..

Create a docker swarm of 3 manager and 2 worker::

    ./utils2devops/bin/swarm.sh -c -m 3 -w 2

Destroy it::

    ./utils2devops/bin/swarm.sh -r 5
