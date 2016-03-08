from datetime import datetime
name = raw_input()"Hello! What is your name?"
now_local = datetime.now()

print "Hello, %s, and welcome to the console!  The current date and time is %s. " % (name, now_local)

