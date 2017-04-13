#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:31:53 2017

@author: parisagandomkaryarandi
"""

from sys import argv

first = raw_input('first = ')
second = raw_input('second = ')
third = raw_input('third = ' )
script = raw_input('script = ' )

script, first, second, third = argv 

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third