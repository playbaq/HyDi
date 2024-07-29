from setuptools import setup
from hydi.hydi import *


setup(
    name='HyDi3',
    version='0.0.1',
    install_requires=[
        'requests',
        'pandas',
        'json',
        'random',
        'importlib-metadata; python_version<"3.10"',
    ],
)