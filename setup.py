#!/usr/bin/env python
<<<<<<< HEAD
# -------------------------------------------------------------------------- #
# Copyright 2010-2011, Indiana University                                    #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#                                                                            #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
# -------------------------------------------------------------------------- #
import setuptools

setuptools.setup(
    setup_requires=['d2to1', 'pbr'],
    d2to1=True)
=======
# -*- coding: utf-8 -*-

import os
import sys

import bootstrap3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = bootstrap3.__version__

if sys.argv[-1] == 'publish':
    os.system('cd docs && make html')
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-bootstrap3',
    version=version,
    description="""Bootstrap support for Django projects""",
    long_description=readme + '\n\n' + history,
    author='Dylan Verheul',
    author_email='dylan@dyve.net',
    url='https://github.com/dyve/django-bootstrap3',
    packages=[
        'bootstrap3',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="Apache License 2.0",
    zip_safe=False,
    keywords='django-bootstrap3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
>>>>>>> 1cba0c85621efa61499076f20e47a8f60a67fae3
