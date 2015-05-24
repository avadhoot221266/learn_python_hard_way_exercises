#just like argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#argv isn't needed
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#just one arguement
def print_one(arg1):
    print "arg1: %r" % arg1

#no argument
def print_nothing():
    print "I got nothing"

print_two('Avadhoot','Kulkarni')
print_one('Avadhoot')
print_nothing()
