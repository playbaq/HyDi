from setuptools import setup
from hydi.hydi import *


setup(
    name='HyDi',
    version='0.0.2',
    install_requires=[
        'requests',
        'pandas',
        'json',
        'random',
        'importlib-metadata; python_version<"3.10"',
    ],
)