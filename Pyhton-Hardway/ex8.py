#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 06:00:56 2017

@author: parisagandomkaryarandi
"""

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter) 
print formatter % (
"I had this thing.",
"That you could type up right.", "But it didn't sing.",
"So I said goodnight."
)

formatter = "%r"
print formatter % 1
print formatter % "one"
print formatter % True