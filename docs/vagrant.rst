
.. include:: links.inc

.. _ref-create_machine:

Create your local cluster of machine
####################################

This playbook will create x nodes machine named name1 to nameN::
the purpose of this script is for local debug or tests, you can after
access to these by::

    vagrant ssh nodeN

required::

    install Vagrant:
    https://www.vagrantup.com/docs/installation/

run::

    export VAGRANT_NODES_COUNT=5
    cd vagrant
    vagrant up

Destroy it::

    export VAGRANT_NODES_COUNT=5
    vagrant destroy -f


.. _ref-create-sw:

Add local nodes in docker-machine
#################################

This script will create a swarm on nodes machine named node1 to nameN,
the purpose of this script is for local debug or tests, you can after
access to these by::

    docker-machine ssh nodeN

required::

    install Docker machine:
    https://docs.docker.com/engine/swarm/

run::

    WORK IN PROGRESS
    docker-machine create \
        --driver generic \
        --generic-ssh-user "ubuntu" \
        --generic-ip-address=35.170.64.155 \
        --generic-ssh-key ~/.ssh/terraform_key \
        node1


