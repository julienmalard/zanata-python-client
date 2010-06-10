#!/usr/bin/env python
"""
Build script for flies-python-client
"""
from setuptools import setup, find_packages

setup (name = "flies-python-client",
    version = '0.0.1',
    packages = find_packages(),
    description = "Flies Python Client.",
    author = 'Jian Ni',
    author_email = 'jni@redhat.com',
    license = 'LGPLv2+',
    platforms=["Linux"],
   
    entry_points = {
	'console_scripts': [
		'flies = fliesclient.flies:main',
	]
    },
    classifiers=['License :: OSI Approved ::  GNU Lesser General Public License (LGPL)',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 ],
)