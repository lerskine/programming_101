
age = raw_input("how old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

from sys import argv

script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "So, you're %s years old, %s tall and %slbs heavy. %s %s %s " % (
    age, height, weight, first, second, third) 
    

