from setuptools import setup

with open("requirements.txt") as rq:
    requirements = rq.read().split('\n')

setup(
    name='Caesar',
    version='0.0.1',
    author='Hussein',
    packages=['CaesarCipher'],
    # license='LICENSE.txt',
    description='Package that apply caesar cipher on string',
    # long_description=open('README.txt').read(),
    install_requires=[requirements],
)