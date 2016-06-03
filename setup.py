#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='cython_demo',
      packages=find_packages(where='cython_demo'),
      package_dir={'': 'cython_demo'},
      version='0.0.1',
      description='try cython for parsing.',
      url='https://github.com/pmart123/cython_demo',
      classifiers=['Private :: Do Not Upload'],
      author='Philip Martin',
      author_email='philip.martin2007@gmail.com',
      install_requires=list(open('requirements.txt').read().strip().split('\r\n')),
      zip_safe=False)
