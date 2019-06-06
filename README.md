# Util2devops

# Infrastructure As Code

A package that contain python 3 functions and class that can be helpfull in the 
all working day. Any help for develop, test, validate, documentation are 
wellcome!

TAKE CARE THIS LIBRARY AND THE TOOLS will do what ever you ask to do, even for 
destroy image, network, container, ...

One of my main principles is not to reinvent the wheel, and if someone has 
already created a function, a class and sharing it, and if I like its implementation, 
I will use this function / class and say a big thank you to this person.
We will use :
- AWS CLI
- CGP tools
- Terraform
- ...

To develop or improve this library you can run it with the env DEBUG_OR_IMPROVE


[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)

# to use lxd_module
## require
```shell
sudo apt-get install python-pylxd lxd
```


# to use terraform_import and aws
## require
```shell
sudo pip3 install --upgrade awscli
export PATH=/home/ec2-user/.local/bin:$PATH
```
Create an AWS account
Install Terraform
https://learn.hashicorp.com/terraform/getting-started/install.html

# Thanks to
    - All contributors of all open sources projects
    