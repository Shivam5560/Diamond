from setuptools import find_packages,setup
from typing import List

hypen_dot_e = '-e .'

def fun(file_path):
    req = []
    with open(file_path) as obj:
        req = obj.readlines()
        req = [x.replace('\n','') for x in req]
        if hypen_dot_e in req:
            req.remove(hypen_dot_e)
        return req

setup(
    name='DiamondPrice',
    version='0.0.1',
    author='Shivam Sourav',
    author_email='shivamsourav2003@gmail.com',
    install_requires=fun('requirements.txt'),
    packages=find_packages()
)