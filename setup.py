from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name='Projekt',
    version='2.0.0',
    author='Michal Bidzinski',
    packages=find_packages(),
    python_requires='>=3.5, <4',
    install_requires=['pyhamcrest', 'parameterized', 'assertpy', 'nose2'],
    extras_require={
        'test': ['coverage']
    },
)