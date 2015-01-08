# coding:utf-8

from setuptools import setup

setup(
    name='juzi-blog',
    version='0.1',
    long_description=__doc__,
    packages=['juzi-blog'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10.1',
        'Flask-PyMongo>=0.3.0'
    ]
)