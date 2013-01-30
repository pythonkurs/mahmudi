from setuptools import setup, find_packages
import sys, os


setup(
name='Owais Mahmudi',
version='0.1',
author='owaism',
author_email='owais.mahmudi@gmail.com',
url='https://github.com/owaismahmudi',
packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
scripts=['scripts/getting_data.py'],
license='GPLv3',
long_description=open('README.txt').read(),
)
