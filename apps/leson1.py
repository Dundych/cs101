# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the values
# defined below.    
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second
print 299792458 *100 / 1000000000

# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0
print speed_of_light / cycles_per_second

# Write python code that defines the variable 
# age to be your age in years, and then prints 
# out the number of days you have been alive.
age = 25
day_in_age = 365.25
print age * day_in_age +283

# Define a variable, name, and assign to it a string that is your name.
name = 'Dmytro'

# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

s = 'audacity'
print "U" + s[2:]    

# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to
# page = '<a href="http://udacity.com">Hello world</a>'
# that your code still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
first_quote = page.find('"', start_link)
second_quote = page.find('"', first_quote + 1)
url =  page[first_quote + 1:second_quote]

print url


# Write Python code that stores the distance 
# in meters that light travels in one 
# nanosecond in the variable, nanodistance. 

# These variables are defined for you:

speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion

# After your code,running
# print nanodistance
# should output 0.2998

# Note that nanodistance must be a decimal number.

# ASSIGN nanodistance BELOW this line
nanodistance = speed_of_light / nano_per_sec



print nanodistance

