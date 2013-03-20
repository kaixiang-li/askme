import sys
from setuptools import setup, find_packages

install_requires = ['versiontools', 'mako', 'termcolor']

setup(
    name = 'askme',
    description = 'A tool to ease the tedious tasks of doing console input and output with low-level methods like raw_input().',
    author = 'Krazy Lee',
    author_email = 'lixiangstar@gmail.com',
    packages = find_packages(exclude=['*.test.*', '*.test']),
    version = ':versiontools:askme:',
    install_requires = install_requires,
    license = 'BSD',
    url = 'http://github.com/krazylee/askme',
    package_data = {'':['README']},
    classifiers = [
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
    ]
)
