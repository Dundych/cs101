#---1---
# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


print factorial(0)
#>>> 1

print factorial(5)
#>>> 120

print factorial(10)
#>>> 3628800
#---2---# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
           return is_palindrome(s[1:len(s)-1])
           
        else:
            return False
 
print 'abba'[1:len('abba')-1]
 
 
print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True

#---3---
# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >1:
        return fibonacci(n-1)+fibonacci(n-2)




print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610
#---4---
#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    thatF = 0
    nextF = 1
    for i in xrange(n):
        buf = thatF
        thatF = nextF
        nextF = buf +thatF
    return thatF



print fibonacci(36)
#>>> 14930352
