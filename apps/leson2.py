﻿#----------------------1---------------------------
# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).

def square(num):
    return num * num




# To test your procedure, uncomment the print 
# statement below, by removing the hash mark (#) 
# at the beginning of the line.

# Do not remove the # from in front of the line 
# with the arrows (>>>). Lines which begin like 
# this (#>>>) are included to show the results
# you should see when run your procedure.

print square(5)
#>>> 25

#----------------------2---------------------------
# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.


def sum3(num1, num2, num3):
    return num1 + num2 + num3






print sum3(1,2,3)
#>>> 6

print sum3(93,53,70)
#>>> 216


#----------------------3-----------------------
# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.


def abbaize(s1, s2):
    return s1+s2*2+s1






print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'

#------------------------4-----------------------------

# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.


def find_second(s1, s2):
    return s1.find(s2, s1.find(s2) + 1)





danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
#>>> 25

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
#>>> 13