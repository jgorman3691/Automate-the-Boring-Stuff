# This file generates the questionsdatetime A combination of a date and a time. Attributes: ()

import random
random.seed(3691)

# Questions is used for individual questions, total holds the dict object

question = {}
remaining = []
total = {}

# This section starts off the process.  I was going to make a list and take correct answers off, but fuck it
# We read from the dictionary file, put it into a dictionary, and close the file


total = open('sandc.py', 'r')
total.readlines()
total.close()

while i < 4:
  remaining[i] = random.randrange(0, 49, 1)
  i += 1
  remaining[i]
  

var = open( 'MasterQ.txt', 'a')