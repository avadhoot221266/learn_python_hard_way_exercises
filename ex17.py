from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#in_file = open(from_file)
#indata = in_file.read()


#indata = (open(from_file)).read()
#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)

#print "Hit Return to continue, Ctrl+c to abort."
#raw_input()

#out_file = open(to_file, 'w')
(open(to_file, 'w')).write((open(from_file)).read())
print "Done"

#print "Here is the data copied"
#out_file = open(to_file)
#print (open(to_file)).read()

print "Closing the files"
#out_file.close()
#in_file.close()
