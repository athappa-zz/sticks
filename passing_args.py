#!/usr/bin/env python

'''
print "How old are you?", 
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight
'''

#All of that can be rewritten like such:

'''
age = raw_input("How old are you?  ")
height = raw_input("How tall are you?  ")
weight = raw_input("How much do you weigh?  ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


from sys import argv
script, first, second, third = argv

print "The script is called:", script
print " Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
'''
prompt = '>'
print "What is your name"
name = raw_input(prompt)


print "Hi, %r" % (name)


