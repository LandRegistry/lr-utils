#!/usr/bin/env python

# see http://bugs.python.org/issue8876
# this is just a quick hack so we can test build in vagrant
import os
if os.environ.get('USER','') == 'vagrant':
  del os.link

from setuptools import setup, find_packages


def requirements():
    with open('./requirements.txt', 'r') as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

setup(name='lrutils',
      version='0.1.3',
      description='Utilities for LR Flask apps',
      author='Land Registry',
      author_email='paul.trelease@digital.landregistry.gov.uk',
      url='https://github.com/LandRegistry/lr-utils',
      download_url = 'http://github.com/LandRegistry/lr-utils/tarball/alpha',
      packages=find_packages(exclude=['tests']),
      zip_safe=False,
      include_package_data=True,
      license='MIT',
      platforms='any',
      classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.7',
        ),
      install_requires=requirements(),
)
