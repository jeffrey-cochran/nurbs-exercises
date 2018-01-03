from distutils.core import setup
from setuptools import find_packages


with open('__version__', 'rb') as f:
    version = f.read().strip()


setup(
    name='nurbs-exercises',
    version=version,
    description='nurbs-exercises',
    author='Jeff Cochran',
    author_email='jeffrey.david.cochran@gmail.com',
    packages=find_packages(),
)
