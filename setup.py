#!/usr/bin/env python

from setuptools import setup

setup(name='sqlcmd',
      version='0.1',
      description="Pure Python alternative to SQLCMD.EXE using PyTDS",
      long_description=open("README.md").read() + "\n"
      + open("AUTHORS.md").read() + "\n" + open("CHANGES.md").read(),
      url='https://github.com/ccpgames/sqlcmd',
      py_modules=['sqlcmd'],
      entry_points={"console_scripts": ["sqlcmd = sqlcmd:main"]},
      install_requires=['python-tds>=1.7.2'],
      license='GNU GPLv3'
      )
