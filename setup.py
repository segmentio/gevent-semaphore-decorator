from setuptools import setup
import os

setup(
    name = 'gevent_semaphore_decorator',
    version = '0.2.0',
    packages=[
        'gevent_semaphore_decorator'
    ],
    install_requires=[
        'gevent>=1'
    ]
)
