try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name='concierge_app',
    version='0.1.8',
    packages=['concierge', 'concierge.models', 'concierge.controller'],
    # You could use find_packages if setuptools is installed. 
    # packages=find_packages(),
    package_data={ 'concierge': ['templates/*.txt'] },
    license='GNU',
    author='hidetan',
    author_email='example@example.com',
    # You can specify install_requires if setuptools is installed
    # install_requires=['termcolor==1.1.0'],
    long_description=open('README.txt').read(),
)
