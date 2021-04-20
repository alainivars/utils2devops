#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test it with:

cddu
./utils2devops/bin/docker-machine-cluster.sh -c 3
cd ansible/swarm
ansible all -i inventories/hf_docker_machine.py -m ping
cd ../..
./utils2devops/bin/docker-machine-cluster.sh -d 3
"""
from __future__ import (absolute_import, division, print_function)
import argparse
import subprocess
try:
    import json
except ImportError:
    import simplejson as json

# Docker-machine (DEPRECATED)

DOCUMENTATION = '''
    name: hf_docker_machine
    plugin_type: inventory
    version_added: '2.8'
    author:
      - Alain Ivars <alainivars@gmail.com>
    short_description: Ansible dynamic inventory plugin for Docker machine nodes.
    requirements:
        - python >= 2.7
        - L(Docker SDK for Python,https://docker-py.readthedocs.io/en/stable/) >= 1.10.0
    extends_documentation_fragment:
        - constructed
    description:
        - Reads inventories from Docker machine.
    options:
        host:
            description:
                - TODO.
'''

EXAMPLES = '''
# Minimal example using local host
plugin: hf_docker_machine
host: unix://var/run/docker.sock

# Minimal example using remote host
plugin: hf_docker_machine
host: tcp://my-docker-host:2375

# Minimal example using remote host
plugin: hf_docker_machine
$ ansible -i ansible/inventories/hf_docker_machine.py machinename -m ping
'''


class HfDockerMachineInventory(object):

    def __init__(self):
        self.args = None
        self.inventory = {'_meta': {'hostvars': {}}}
        self.read_cli_args()
        if self.args.list:
            self.inventory = self.generate_inventory()
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            pass
        print(json.dumps(self.inventory))

    def generate_inventory(self):
        machines_status = hf_docker_machine('ls').decode().splitlines()
        for machine_status_str in machines_status:
            machine_status = machine_status_str.split()
            if machine_status[3] == 'Running':
                machines_desc = json.loads(hf_docker_machine('inspect', machine_status[0]).decode())
                # because All machines use different credential
                group_name = machines_desc['Driver']['MachineName'].replace('-', '').replace('_', '')
                self.inventory[group_name] = {
                    'hosts': [machines_desc['Driver']['IPAddress']],
                    'group_vars': {
                        'ansible_ssh_user': machines_desc['Driver']['SSHUser'],
                        'ansible_ssh_port': '22',
                        'ansible_ssh_private_key_file': machines_desc['Driver']['SSHKeyPath']
                    }
                }
            # inventory = {
        #     'machines': {
        #         'hosts': ['192.168.99.100', '192.168.99.101', '192.168.99.102'],
        #         'group_vars': {
        #             'ansible_ssh_user': 'docker',
        #             'ansible_ssh_port': '39193',
        #             'ansible_ssh_private_key_file': '/home/alain/.docker/machine/machines/server.1/id_rsa'
        #         }
        #     },
        #     # 'master': {
        #     #         'hosts': ['192.168.99.100'],
        #     #         'group_vars': {
        #     #             'ansible_ssh_user': 'docker',
        #     #             'ansible_ssh_port': '39193',
        #     #             'ansible_ssh_private_key_file': '/home/alain/.docker/machine/machines/server.1/id_rsa'
        #     #         }
        #     # },
        #     # 'managers': {
        #     #         'hosts': ['192.168.99.100'],
        #     #         'group_vars': {
        #     #             'ansible_ssh_user': 'docker',
        #     #             'ansible_ssh_port': '39193',
        #     #             'ansible_ssh_private_key_file': '/home/alain/.docker/machine/machines/server.1/id_rsa'
        #     #         }
        #     # },
        #     # 'workers': {
        #     #         'hosts': ['192.168.99.101', '192.168.99.102'],
        #     #         'group_vars': {
        #     #             'ansible_ssh_user': 'docker',
        #     #             'ansible_ssh_port': '39193',
        #     #             'ansible_ssh_private_key_file': '/home/alain/.docker/machine/machines/server.1/id_rsa'
        #     #         }
        #     # },
        #     # 'gateway': {},
        #     # 'ungrouped': {},
        #     'all': {
        #         'children': [
        #             'machines',
        #             # 'master',
        #             # 'managers',
        #             # 'workers',
        #             # 'gateway',
        #             # 'ungrouped',
        #         ]
        #     },
        #     '_meta': {
        #         'hostvars': {
        #             '192.168.99.100': {
        #                 'host_specific_var': 'foo'
        #             },
        #             '192.168.99.101': {
        #                 'host_specific_var': 'bar'
        #             },
        #             '192.168.99.102': {
        #                 'host_specific_var': 'bo'
        #             }
        #         }
        #     }
        # }
        return self.inventory

    def read_cli_args(self):
        parser = argparse.ArgumentParser(
            description='Generate an Ansible Inventory from Docker Machine inspect'
        )
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()


def hf_docker_machine(*args):
    return subprocess.check_output(['docker-machine'] + list(args)).strip()


# def dminspect(mcn):
#     return hf_docker_machine('inspect', mcn).decode()
#
#
# def get_host_and_vars(m):
#     hosts = dminspect(m)
#     ssh_vars = {
#         'ansible_ssh_user': dminspect('{{.Driver.SSHUser}}', m),
#         'ansible_ssh_port': dminspect('{{.Driver.SSHPort}}', m),
#         'ansible_ssh_private_key_file': dminspect('{{.Driver.SSHKeyPath}}', m)
#     }
#     data = {'hosts': hosts, 'group_vars': ssh_vars}
#     return data

if __name__ == '__main__':
    HfDockerMachineInventory()
