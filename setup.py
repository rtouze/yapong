#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup (
        name='yapong',
        version='1.0',
        autho='Josh',
        description='A classical Pong clone using pygame',
        install_requires=['pygame'],
        long_description=open('README.markdown').read(),
        classifiers=[
            "License :: WTFPL",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.6",
            "Topic :: Games",
            ],
        packages=find_packages(),
        include_package_data=True,
        entry_points={
            'console_scripts': ['yapong = yapong.yapong:main']
            },
        license='WTFPL'
        )

