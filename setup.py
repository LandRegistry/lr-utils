#!/usr/bin/env python

# see http://bugs.python.org/issue8876
# this is just a quick hack so we can test build in vagrant
import os
if os.environ.get('USER','') == 'vagrant':
  del os.link

from setuptools import setup, find_packages

setup(name='lrutils',
      version='0.1',
      description='Utilities for LR Flask apps',
      author='Land Registry',
      author_email='adam.shimali@digital.cabinet-office.gov.uk',
      url='https://github.com/LandRegistry/lr-utils',
      download_url = 'http://github.com/LandRegistry/lr-utils/tarball/alpha',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      license='MIT',
      platforms='any',
      install_requires=['passlib==1.6.2', 'py-bcrypt==0.4'],
      classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.7',
        ),
)
