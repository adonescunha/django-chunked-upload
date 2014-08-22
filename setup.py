#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-chunked-upload
# https://github.com/adonescunha/django-chunked-upload

# Copyright (c) 2014 Adones Cunha adonescunha@gmail.com


from setuptools import setup

from support import version


setup(
    name='django-chunked-upload',
    version='0.1.0',
    description='Chunked upload Django views implementation using django-resumable.',
    author='Adones Cunha',
    author_email='adonescunha@gmail.com',
    url='https://github.com/adonescunha/django-chunked-upload',
    packages=[
        'chunked_upload'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Testing'
    ],
    install_requires=[
        'django-resumable'
    ]
)
