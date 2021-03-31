#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 04:35:49 2021

@author: lukashentschel
"""
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