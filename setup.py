from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='myapp',
      version=version,
      description="desc",
      long_description="""\
desclong""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='dfd',
      author='mahmudi',
      author_email='owais.mahmudi@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
