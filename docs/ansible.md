# Ansible

## Introduction

### Install/update
todo
### First example
Check everything is fine.
#### Update the inventory file
Update inventories/local-inventory and add your machines
```shell
cd ansible/lab
vi inventories/local-inventory
[local]
localhost   ansible_connection=local

[lab]
192.168.0.16    # beowolf016.hf.ais       beowolf016
192.168.0.26    # beowolf026.hf.ais       beowolf026

[pvenodes]
192.168.0.26    # beowolf026.hf.ais       beowolf026
```
Now the test
```shell
ansible pvenodes -i inventories/local-inventory -m ping --user=root -k
SSH password: 
192.168.0.26 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

