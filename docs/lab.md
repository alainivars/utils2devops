# lab
Here we will provision/update the lab

## Examples deployment commands

Deploy on every "pvenodes" defined in local-inventory.
```shell
cd ansible
ansible-playbook pvenodes -i lab/inventories/local-inventory docker.yml
```
Deploy on 192.168.0.26 with user root, ask password.
```shell
cd ansible
ansible-playbook -i 192.168.0.26, base-provision.yml --user=root -k
```
Now create the file /home/a/.ssh/ansible_service and put inside the content of your NEW_USER_TOKEN_SECRET.
You can now use it for deployment on the pve hosts.
Deploy on 192.168.0.26 with user "service" using ssh key.
```shell
cd ansible
ansible-playbook -i 192.168.0.26, base-provision.yml --user=service --private-key /home/a/.ssh/ansible_service
```

## To create a system user named john and add it as a PAM user in Proxmox, you would follow these steps:
Create the system user:
```shell
adduser john
passwd john
```
Add the PAM user to Proxmox:
```shell
pveum user add john@pam
```
Set the role for the user:
```shell
pveum acl modify / --roles PVEAdmin --users john@pam
```
