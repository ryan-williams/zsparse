from setuptools import setup, find_packages

setup(
  name='zsparse',
  version='0.1.0',
  url='https://github.com/daletovar/zsparse.git',
  author='Dale Tovar',
  description='A library for zarr compressed sparse matricies',
  packages=find_packages(),
  install_requires=['numpy >= 1.11.1', 'zarr >= 2.3.0', 'scipy >= 1.3.0'],
)
