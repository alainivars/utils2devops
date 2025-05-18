
.. include:: links.inc

.. _ref-create_machine:

Create your local cluster of machine
####################################

If you want use QEMU run
vagrant plugin install vagrant-qemu

This playbook will create x nodes machine named name1 to nameN::
the purpose of this script is for local debug or tests, you can after
access to these by::

    vagrant ssh nodeN

Required::

    install Vagrant:
    https://www.vagrantup.com/docs/installation/

Setup::

    cd vagrant
    your-favorite-editor vagrant.yml

Run::

    vagrant up
    or
    vagrant up --provider qemu

Destroy it::

    vagrant destroy -f


.. _ref-create-sw:
