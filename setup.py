from setuptools import setup, find_packages
from os import path

dir = path.abspath(path.dirname(__file__))
with open(path.join(dir, 'README.md'), encoding='utf-8') as f:
    README = f.read()

setup(
    name='methodes_agile',
    version='1',
    description='Cours AGILE M2',
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=README,
    author='Théo Chennebault',
    author_email='theo.chennebault@le-cab-politique.fr',
    url='https://github.com/ErnestBidouille/agile',
    packages=find_packages(exclude=['tests*']),
    install_requires=['pytest', 'coverage', 'behave'],
)