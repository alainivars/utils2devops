#!/usr/bin/env python

import os
from setuptools import setup, find_packages

from utils2devops.tools.description import get_long_description_from_file
from utils2devops.tools.single_sourcing_package_version import get_version

# doc is here
# https://setuptools.readthedocs.io/en/latest/setuptools.html#installing-setuptools

path = os.path.dirname(os.path.abspath(__file__))
long_description = get_long_description_from_file(path, 'README.rst')


setup(
    name='utils2devops',
    version=get_version('docs'),
    author='Alain IVARS',
    url='http://github.com/alainivars/utils2devops',
    author_email='alainivars@gmail.com',
    license='Apache License 2.0',
    description='''
    contain python 3 functions and class that can be helpful in the all 
    working day
    ''',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    keywords='''
    Devops Docker Kubernetes Terraform Lxd Lxc Aws
    ''',
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.10",
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=[
        # 'boto3',  # AWS
        # # https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-init.html
        # 'aws-sam-cli',  # AWS
        # 'pylxd',  # LXD
    ]
)