# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(  name='fizzbuzz',
    	version='1.0',
    	description='Fizzbuzz applied to a Fibonacci series.',
		long_description=readme,
		author='Ben Rollin',
		url='https://github.com/kennethreitz/samplemod',
		license=license,
		packages=find_packages(exclude=('tests',))
)
