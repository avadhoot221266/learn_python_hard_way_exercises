from sys import argv

print "First fruit: "
first = raw_input()

print "Second fruit: "
second = raw_input()

print "Third fruit: "
third = raw_input()

script, first, second, third = argv


print "This is the: ", script
print "The first variable is: ", first
print "The second variable is: ", second
print "The third variable is: ", third
