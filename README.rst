
Welcome to Utils2devops documentation!
=====================================

Infrastructure As Code
======================

A package that contain python 3 functions and class that can be helpfull in the 
all working day. Any help for develop, test, validate, documentation are 
welcome!

TAKE CARE THIS LIBRARY AND THE TOOLS will do what ever you ask to do, even for 
destroy image, network, container, ...

One of my main principles is not to reinvent the wheel, and if someone has 
already created a function, a class and sharing it, and if I like its implementation, 
I will use this function / class and say a big thank you to this person in all respect of the Copyright and the Licence.
This library is in development and the folder structure will change certainly

We will use :
- AWS CLI
- CGP tools
- Terraform
- ...

To develop or improve this library you can run it with the env DEBUG_OR_IMPROVE


To use lxd_module
#################
require::

    sudo apt-get install python-pylxd lxd


To use terraform_import and aws
###############################
require::

    sudo pip3 install --upgrade awscli
    export PATH=/home/ec2-user/.local/bin:$PATH

Create an AWS account (it's free)::

    https://aws.amazon.com/


Install Terraform::

    https://learn.hashicorp.com/terraform/getting-started/install.html


.. _`Utils2devops`: https://github.com/alainivars/utils2devops
.. _`Issue Utils2devops`: https://github.com/alainivars/utils2devops/issues
.. _`Readthedoc`: https://utils2devops.readthedocs.io/en/latest/
.. _`Github`: https://github.com/alainivars/utils2devops
.. _`Releases notes`: https://github.com/alainivars/utils2devops/blob/master/docs/releases_notes.rst
