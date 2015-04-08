#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='auto_facebook',
      version='0.0.0',
      packages=find_packages(),
      package_data = {
          # If any package contains *.txt or *.rst files, include them:
          '': ['*.json'],

          },
      install_requires=['robotframework-selenium2library','robotframework-faker'],
      )
