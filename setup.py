
from setuptools import setup, find_packages

setup(
    name='python_package_example',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/BillMills/python-package-example',
    author='Marco Kulueke',
    author_email='myemail@example.com'
)
