#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import highlighter

setup(
    name = 'django-highlighter',
    version = ":versiontools:highlighter:",
    description = "Generic model mixin for highlight Models",
    long_description = "",
    keywords = 'django, model',
    author = 'Jesús Espino García',
    author_email = 'jespinog@gmail.com',
    url = 'https://github.com/jespino/django-highlighter',
    license = 'BSD',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[
        'distribute',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
