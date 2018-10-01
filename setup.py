#!/usr/bin/env python

import os
from setuptools import setup, find_packages


here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README.md'))
long_description = f.read().strip()
f.close()


setup(
    name='utils2devops',
    version='0.0.1',
    author='Alain IVARS',
    url='http://github.com/alainivars/utils2devops',
    author_email='alainivars@gmail.com',
    license='Apache License 2.0',
    description='''
    contain python 3 functions and class that can be helpfull in the all 
    working day
    ''',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='''
    Devops Docker Kubernete Juju Lxd Lxc Aws
    ''',
    zip_safe=False,
    test_suite='setuptest.setuptest.SetupTestSuite',
    include_package_data=True,
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache License, Version 2.0 (Apache-2.0)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)