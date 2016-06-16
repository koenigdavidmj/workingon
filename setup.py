#!/usr/bin/env python

from distutils.core import setup

setup(name='workingon',
      version='0.0.1',
      description="Easy management of multiple-device development harnesses",
      author='David Koenig',
      author_email='koenigdavidmj@gmail.com',
      scripts=['scripts/workingon'],
      packages=['workingon'],
      package_dir={'workingon': 'src/workingon'},
)
