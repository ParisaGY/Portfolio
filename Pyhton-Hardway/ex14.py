#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:14:00 2017

@author: parisagandomkaryarandi
"""

from sys import argv 
script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

print "Do you like me %s?" % user_name,
likes = raw_input(prompt)

print "Where do you live %s?" % user_name,
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "How old are you %s?" % user_name,
old = raw_input(prompt)

print """
Alright, so you are %r years old and you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % ( old, likes, lives, computer)