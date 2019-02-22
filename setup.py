from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='cva_apps',
    version=version,
    description='CVA APPs Presented By CVA IT SUPPORT',
    author='CVA IT SUPPORT',
    author_email='info@cvaitsupport.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
