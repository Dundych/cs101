#----------------------1---------------------------
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


#----------------------------5-------------------------
# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(a, b):
    if a < b :
        a = b
    return a





print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3

#--------------------------------------6-7--------------------
# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(name):
    return name.find('D') * name.find('N') == 0



print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False

#-----------------8---------------------------------

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a, b, c):
    result = a
    if  result < b:
        result = b
    if  result < c:
        result = c
    return result
        





print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9

#----------------------9---------------------
# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(num) :
    i = 1
    while i < num + 1 :
        print i
        i = i + 1
                  
   



print_numbers(9)
#>>> 1
#>>> 2
#>>> 3

#-------------------10-----------------------

# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    res = 1
    while n > 1:
        res = res * n
        n = n - 1
    return res




print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

#-----------------------------11----------------

# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
                 

#----------------------------Home Work-----------------------
# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is anhttps://www.udacity.com/course/viewer uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

# Make sure your procedure has a return statement.

def udacify(s):
    return 'U' + s






# Remove the hash, #, from infront of print to test your code.

print udacify('dacians')
#>>> Udacians

print udacify('turn')
#>>> Uturn

print udacify('boat')
#>>> Uboat


#---------------------------------------2------------------------------
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    if a == biggest(a,b,c):
       return bigger(b, c)
    if b == biggest(a,b,c):
       return bigger(a, c)
    else:
       return bigger(a, b)


print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

#--------------------------3--------------------------
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(num):
    while num > 0:
        print num
        num = num -1
    print "Blastoff!"





countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!


#--------------------------------------4---------------------
# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.


def find_last(sStr, tStr):
    
    pos = -1
    result = -1
    while True:
        pos = sStr.find(tStr, pos +1)
        if pos == -1:
            break
        result = pos
    return result





print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0

















