from sys import argv #imports argv module from the python system

script, filename = argv #passing the argumenets

txt = open(filename) #open the file

print "Here is the file %r: " % filename
print txt.read() #read the file

print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
