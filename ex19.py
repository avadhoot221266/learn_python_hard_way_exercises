#defining the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "And %d boxes of crackers" % boxes_of_crackers
    print "That's enough for a party."
    print "Get a blanket."

#passing direct arguments
cheese_and_crackers(20, 30)

#passing arguments by declaring them frist
amount_of_cheese = 50
amount_of_crackers = 60

print "\nUpdate! Update!\n"
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#passing arguments using maths
print "\nRoger that\n"
cheese_and_crackers(20 + 30, 30*2)

#passing arguements by declaring and operating them
print "\nFinal Call\n"
cheese_and_crackers(amount_of_cheese/2, amount_of_crackers*2)

#my own function: calculating the cheese left
def cheese_left(original_cheese, used_cheese):
    print "Originally we had %d cubes of cheese" % original_cheese
    print "You ate %d cubes of cheese" %used_cheese
    print "That leaves us with %d cubes of cheese" % (
    original_cheese-used_cheese)

cheese_left(20, 15)

cheese_left(90/3, 80/3)

old = 110
new = 90

cheese_left(old, new)
