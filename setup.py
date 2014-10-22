#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='lrutils',
      version='0.1',
      description='Utilities for LR Flask apps',
      author='Land Registry',
      author_email='adam.shimali@digital.cabinet-office.gov.uk',
      url='https://github.com/LandRegistry/lr-utils',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      license='MIT',
      platforms='any',
      install_requires=['passlib==1.6.2', 'py-bcrypt==0.4', 'python-dateutil==2.2'],
)
