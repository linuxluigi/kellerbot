# -*- coding: utf-8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os
import codecs
from setuptools import setup, find_packages

# Save version and author to __meta__.py
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'src', 'kellersensortelegrambot', '__meta__.py')
meta = '''# Automatically created. Please do not edit.
__version__ = '%s'
__author__ = 'Steffen Exler'
''' % version
with open(path, 'w') as F:
    F.write(meta)

setup(
    # Basic info
    name='kellersensortelegrambot',
    version=version,
    author='Steffen Exler',
    author_email='steffen.exler@pm.me',
    url='',
    description='A short description for your project.',
    long_description=codecs.open('README.rst', 'rb', 'utf8').read(),

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
    ],

    entry_points={
        "console_scripts": ['keller = kellersensortelegrambot.__main__:main']
    },

    # Packages and dependencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        "python-telegram-bot >= 10.1.0",
        # "git+git://github.com/adafruit/Adafruit_Python_DHT.git",
        "RPi.GPIO >= 0.6.3",
    ],
    dependency_links=['http://github.com/adafruit/Adafruit_Python_DHT/tarball/master#egg=package-1.0'],
    extras_require={
        'dev': [
            'python-boilerplate[dev]',
        ],
    },

    # extra files
    data_files=[('/lib/systemd/system/', ['scripts/keller.service'])],

    # Other configurations
    zip_safe=False,
    platforms='any',
)
