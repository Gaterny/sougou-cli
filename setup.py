#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf8') as f:
    long_description = f.read()
setup(
    name='sougou-cli',
    version='1.0.0',
    description=(
        'a simple command line translation tool based on sougou api '
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Gaterny',
    author_email='scusong@foxmail.com',
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    install_requires=[
            'requests',
        ],
    url='https://github.com/Gaterny/sougou-cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'sg = sougou.sougou:main',
        ]
    }
)