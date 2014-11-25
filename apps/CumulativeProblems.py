# Question 1: Pick One

# Define a procedure, pick_one, that takes three inputs: a Boolean 
# and two other values. If the first input is True, it should return 
# the second input. If the first input is False, it should return the 
# third input.

# For example, pick_one(True, 37, 'hello') should return 37, and
# pick_one(False, 37, 'hello') should return 'hello'.

def pick_one(flag, a, b):
    if flag:
        return a
    else:
        return b
    



print pick_one(True, 37, 'hello')
#>>> 37

print pick_one(False, 37, 'hello')
#>>> hello

print pick_one(True, 'red pill', 'blue pill')
#>>> red pill

print pick_one(False, 'sunny', 'rainy')
#>>> rainy

# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive 
# integer n and returns the nth triangular number.

def triangular(n):
    res = 0
    for i in xrange(n):
        res+=(i+1)
    return res



print triangular(1)
#>>>1

print triangular(3)
#>>> 6

print triangular(10)
#>>> 55

# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(s):
    while s.find('<') != -1:
       s = remove_first_tag(s)
    return s.split()

def remove_first_tag(s):
    tag = s[s.find("<"):s.find(">")+1]
    s = s[:s.find(tag)] +' '+ s[s.find(tag)+len(tag):]
    return s

print remove_first_tag('''Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']