from setuptools import setup
import HyDi.src.hydi.hydi as hydi


setup(
    name='HyDi',
    version='0.0.1',
    install_requires=[
        'requests',
        'pandas',
        'json',
        'random',
        'importlib-metadata; python_version<"3.10"',
    ],
)