#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 07:53:03 2017

@author: parisagandomkaryarandi
"""
## define variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car 
average_passengers_per_car = passengers / cars_driven


## print the information
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


print "I am", 35, "years old"

## drill

Hens = 25 + 30 / 6
Roosters = 100 - 25 * 3 % 4
print ("I will now count my chickens:")
print "Hens=", Hens
print "Roosters", Roosters



