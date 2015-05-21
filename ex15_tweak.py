from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %s: " % filename
print txt.read()
