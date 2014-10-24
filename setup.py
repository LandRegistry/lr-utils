#!/usr/bin/env python

from setuptools import setup, find_packages


def requirements():
    with open('./requirements.txt') as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

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
      install_requires=requirements(),
)
