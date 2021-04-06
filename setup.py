#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
setup(
    name = 'duplicateFinder',
    version = '0.1.0',
    packages = ['duplicateFinder'],
    entry_points = {
        'console_scripts': [
            'duplicateFinder = duplicateFinder.__main__:main'
        ]
    })