from distutils.core import setup
from setuptools import find_packages

setup(
    name='tetos',
    version='0.1dev',
    author='Artur Stepniak',
    author_email='aart.st@gmail.com',
    packages=find_packages(),
    scripts=['script/tetos.py'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read()
)
