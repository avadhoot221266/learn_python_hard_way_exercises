from sys import argv

script, filename = argv

print "We're going to erase the file %r: " % filename
print "If you don't want, please press CTRL-C"
print "If you want that, press RETURN"

raw_input("> ")

print "Opening the file..."

target = open(filename, 'w')

print "Truncating the file. Bbye!"

target.truncate()

print "%r is now truncated. Let's write something in it." % filename

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "Ok, great! Let's write."

#target.write(line1 + "\n" + line2 + "\n" + line3) # 1st way to do it

target.write ("%s\n%s\n%s\n" % (line1, line2, line3)) # 2nd way

#target.write("\n")

#target.write(line2)
#target.write('\n')

#target.write(line3)
#target.write('\n')

print "Let's see if it's written properly."

target = open(filename)
print target.read()

print "Written. Closing the file."
target.close()
