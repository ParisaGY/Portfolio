#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 06:45:38 2017

@author: parisagandomkaryarandi
"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""" 
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat



while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,


fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
''' 
print tabby_cat
print persian_cat
print backslash_cat
print "%s" % fat_cat
