#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://bttv.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='bttv',
    version='0.1.0',
    description='Tools for a implementing time-varying Bradley-Terry rankings',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author="Heejong Bong <blueconet@gmail.com>, Wanshan Li <wanshanl@andrew.cmu.edu>, Shamindra Shrotriya <shamindra.shrotriya@gmail.com>",
    author_email='shamindra.shrotriya@gmail.com',
    url='https://github.com/shamindras/bttv',
    packages=[
        'bttv',
    ],
    package_dir={'bttv': 'bttv'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='bttv',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
    python_requires='>=3.6',
)
