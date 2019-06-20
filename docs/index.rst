.. Utils2devops documentation master file, created by
   sphinx-quickstart on Sun Jun 16 17:55:07 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: links.inc

Welcome to Utils2devops documentation!
======================================

.. image:: https://api.travis-ci.org/alainivars/utils2devops.svg?branch=master
    :target: http://travis-ci.org/alainivars/utils2devops
    :alt: Build status

.. image:: https://coveralls.io/repos/github/alainivars/utils2devops/badge.svg?branch=master
    :target: https://coveralls.io/github/alainivars/utils2devops?branch=master
    :alt: Test coverage status

.. image:: https://requires.io/github/alainivars/utils2devops/requirements.svg?branch=master
    :target: https://requires.io/github/alainivars/utils2devops/requirements/?branch=master
    :alt: Requirements Status

.. image:: https://img.shields.io/pypi/dm/utils2devops.svg
   :target: https://pypi.python.org/pypi/utils2devops/
   :alt: pypi download

.. image:: https://img.shields.io/pypi/pyversions/utils2devops.svg
   :target: https://pypi.python.org/pypi/utils2devops/
   :alt: python supported

.. image:: https://img.shields.io/pypi/l/utils2devops.svg
   :target: https://pypi.python.org/pypi/utils2devops/
   :alt: licence

.. image:: https://img.shields.io/pypi/v/utils2devops.svg
   :target: https://pypi.python.org/pypi/utils2devops
   :alt: PyPi version

.. image:: https://api.codeclimate.com/v1/badges/1ba86a1707cdb492ddf6/maintainability
   :target: https://codeclimate.com/github/alainivars/utils2devops/maintainability
   :alt: Maintainability

.. image:: https://readthedocs.org/projects/utils2devops/badge/?version=latest
   :target: https://readthedocs.org/projects/utils2devops/?badge=latest
   :alt: Documentation status

.. image:: https://pypip.in/wheel/utils2devops/badge.svg
   :target: https://pypi.python.org/pypi/utils2devops/
   :alt: PyPi wheel


Contents
========
.. toctree::
   :maxdepth: 2
   :caption: How to use it:

   testing
   aws
   lxc_lxd
   releases_notes
   source/modules

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Infrastructure As Code
======================

Utils2devops is a package that contain python 3 functions and class that can be helpfull in the
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

Thanks to::

    - All contributors of all open sources projects

Something disturb you in the code? Don't hesitate to open a an issue and contribute.

Online documentation is here on `Readthedoc`_
Online source code available on `Github`_
