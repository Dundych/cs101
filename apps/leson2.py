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


#---------------------5----------
# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # your code here
    if day == 'Saturday' or day == 'Sunday':
        return True
    return False
    
print weekend('Monday')
#>>> False

print weekend('Sunday')
#>>> True

print weekend('July')
#>>> False

#-------------------------------6---------------------
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(num):
    # Your code here
    p5 = p2 = p1 = 0
    while True:
        if (num - 5) >= 0:
            num = num - 5
            p5 = p5 + 1
        else:
            if (num - 2) >= 0:
                num = num - 2
                p2 = p2 + 1
            else:
                if num >0:
                    p1 = 1
                break
    return p5, p2, p1

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps

#----------------------------7-----------------------

# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def set_range(a, b, c):
    # Your code here
    def bigger(a, b):
        if a > b:
            return a
        return b
    def biggest(a, b, c):
        return bigger(a, bigger(b, c))
    def smaller(a, b):
        if a < b:
            return a
        return b
    def smallest(a, b, c):
        return smaller(a, smaller(b, c))
    return biggest(a, b, c) - smallest(a, b, c)

print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6

#--------------------------------8--------------------------

# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: # 
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #

def fix_machine(debris, product):
    ### WRITE YOUR CODE HERE ###
    pos = 0
    while pos < len(product):
        if debris.find(product[pos]) == -1:
           return  "Give me something that's not useless next time."
        pos = pos +1
    return product

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'

#---------------------------9------------------------

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    def isLeapYear(year):
        if (year % 4) != 0:
            return 0
        if (year % 100) != 0: 
            return 1
        if (year % 400) != 0:
            return 0
        return 1
    
    def dayOnMonth(m):
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m ==12:
            return 31
        if m == 4 or m == 6 or m == 9 or m == 11:
            return 30
        if m == 2:            
            return 28
    def dayFromStartYear(year, month, day) :
        result = 0
        countMonth = 1
        while countMonth < month:
            if countMonth == 2:
                result = result + isLeapYear(year)
            result = result + dayOnMonth(countMonth)
            countMonth = countMonth + 1
        return result + day
    
    result = 0
    year = year1
    while year2 - year > 1:
        if isLeapYear(year):
            result = result + 1
        result = result + 365
        year =  year + 1
    if year2 - year1 > 0:
        result = result + 365 + isLeapYear(year1) - dayFromStartYear(year1, month1, day1)
        result = result + dayFromStartYear(year2, month2, day2)
    else:
        result = dayFromStartYear(year2, month2, day2) - dayFromStartYear(year1, month1, day1)
    return result
# Test routine 

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
print daysBetweenDates(2011,6,30,2012,6,30)
print daysBetweenDates(2012,1,1,2012,2,28)











