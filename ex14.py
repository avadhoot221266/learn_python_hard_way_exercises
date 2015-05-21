from sys import argv

script, user_name, age = argv
prompt = 'Answer - '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'm gonna ask you a few questions"
print "Do you like me, %s" % user_name
likes = raw_input(prompt)

print "Where do you live, %s" % user_name
lives = raw_input(prompt)

print "What computer do you have?"
computer = raw_input(prompt)

print "Do you play super mario? Difficult question for a %s years old ;)" % age
mario = raw_input(prompt)

print """
Okay %s, so you said %r about liking me.
You live in %r. Cool place!
And you have %r computer. Nice.
Playing mario is good. You said %r, It's a game for kids to be honest :D
""" % (user_name, likes, lives, computer, mario)
