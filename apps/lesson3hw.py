#------1-----------
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(mas):
    res = 1
    for el in mas:
        res *= el
    return res


print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1

#----------2----------------

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(a):
    res = 0
    for el in a:
        if res < el:
            res = el
    return res




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0
#------3-------
# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(a):
    st = 0
    fees = 0
    for el in a:
       st += el[1]
       fees += (el[1] * el[2])
    return st, fees
    

print total_enrollment(udacious_univs)
#>>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.

print total_enrollment(usa_univs)
#>>> (77285,3058581079)

#------------4------------------
# The web crawler we built at the end of Unit 3 has some serious
# flaws if we were going to use it in a real crawler. One
# problem is if we start with a good seed page, it might
# run for an extremely long time (even forever, since the
# number of URLS on the web is not actually finite). This
# question and the following one explore two different ways
# to limit the pages that it can crawl.

# Modify the crawl_web procedure to take a second parameter,
# max_pages, that limits the number of pages to crawl.
# Your procedure should terminate the crawl after
# max_pages different pages have been crawled, or when
# there are no more pages to crawl.

# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
            if len(crawled) >= max_pages:
                break
    return crawled

print crawl_web("http://www.udacity.com/cs101x/index.html",1) 
#>>> ['http://www.udacity.com/cs101x/index.html']

print crawl_web("http://www.udacity.com/cs101x/index.html",3) 
#>>> ['http://www.udacity.com/cs101x/index.html', 
#>>> 'http://www.udacity.com/cs101x/flying.html', 
#>>> 'http://www.udacity.com/cs101x/walking.html']

#print crawl_web("http://www.udacity.com/cs101x/index.html",500) 
#>>> ['http://www.udacity.com/cs101x/index.html', 
#>>> 'http://www.udacity.com/cs101x/flying.html', 
#>>> 'http://www.udacity.com/cs101x/walking.html', 
#>>> 'http://www.udacity.com/cs101x/crawling.html', 
#>>> 'http://www.udacity.com/cs101x/kicking.html']

#---------------------5-------------------------
# 
# This question explores a different way (from the previous question)
# to limit the pages that it can crawl.
#
#######

# THREE GOLD STARS #
# Yes, we really mean it!  This is really tough (but doable) unless 
# you have some previous experience before this course.


# Modify the crawl_web procedure to take a second parameter,
# max_depth, that limits the depth of the search.  We can 
# define the depth of a page as the number of links that must
# be followed to reach that page starting from the seed page,
# that is, the length of the shortest path from the seed to
# the page.  No pages whose depth exceeds max_depth should be
# included in the crawl.  
# 
# For example, if max_depth is 0, the only page that should
# be crawled is the seed page. If max_depth is 1, the pages
# that should be crawled are the seed page and every page that 
# it links to directly. If max_depth is 2, the crawl should 
# also include all pages that are linked to by these pages.
#
# Note that the pages in the crawl may be in any order.
#
# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
        '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return  ('<a href="http://top.contributors/elssar.html">'
        '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
        '<a href="http://top.contributors/johang.html">'
        '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
        '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
        '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return  '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return  '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    while max_depth >= 0:
        buf = []
        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled:
                buf += get_all_links(get_page(page))
                #union(tocrawl, get_all_links(get_page(page)))
                crawled.append(page)
        tocrawl += buf            
        max_depth -= 1
    return crawled

print crawl_web("http://www.udacity.com/cs101x/index.html",0)
#>>> ['http://www.udacity.com/cs101x/index.html']

print crawl_web("http://www.udacity.com/cs101x/index.html",1)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html']

print crawl_web("http://www.udacity.com/cs101x/index.html",50)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']

print crawl_web("http://top.contributors/forbiddenvoid.html",2)
#>>> ['http://top.contributors/forbiddenvoid.html',
#>>> 'http://top.contributors/graemeblake.html',
#>>> 'http://top.contributors/angel.html',
#>>> 'http://top.contributors/dreyescat.html',
#>>> 'http://top.contributors/johang.html',
#>>> 'http://top.contributors/charlzz.html']

print crawl_web("A1",3)
#>>> ['A1', 'C1', 'B1', 'E1', 'D1', 'F1']
# (May be in any order)

#----6-----

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def is_corect(some_list):
    list_valids_value =[]
    n = len(some_list)
    while n:
       list_valids_value.append(n)
       n -= 1
    unic = []
    while some_list:
        el = some_list.pop()
        if (el in unic) or (el not in list_valids_value):
           return False
        unic.append(el)
    return True


def is_valid(list_of_lists):
    for OneList in list_of_lists:
        if not is_corect(OneList):
           return False
    return True

def sort_by_columns(list_of_lists):
    res = []
    n = len(list_of_lists)
    while n:
        row = []
        for OneList in list_of_lists:
            row.append(OneList[-n])
        res.append(row)
        n -= 1
    return res
        

def check_sudoku(square):
    for el in square:
        if len(el) != len(square):
            return False
    list_rows = square
    list_columns = sort_by_columns(square)
    if is_valid(list_rows) and is_valid(list_columns):
        return True
    return False


print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False

#-----7----

# Investigating adding and appending to lists

# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5]
list2.append(5)

# to check, you can print them out using the print statements below.

#print list1
#print list2

# What is the difference between these two pieces of code?

def proc(mylist):
    mylist = mylist + [6]

def proc2(mylist):
    mylist.append(6)

def proc3(mylist):
    mylist += [6]

# Can you explain the results given by the four print statements below? Remove
# the hashes # and run the code to check.

#print list1
#proc(list1)
#print list1

#print list2
#proc2(list2)
#print list2

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4]
list3 += [5]

# Does this behave like list1 = list1 + [5] or list2.append(5)? Write a
# procedure, proc3 similar to proc and proc2, but for +=. When you've done
# that check your conclusion using the print-procedure call-print code as
# above.

# What happens when you try:

list1 = list1 + [7,8,9]
list2.append([7,8,9])
list3 += [7,8,9]

# When you've understood the difference between the three methods,
# write a procedure list_test which takes three lists as inputs. You should
# mutate the first input list to include 'a' as the last entry, mutate the
# second to include the entries 'a', 'b', 'c' and finally the last list should
# not be mutated but a copy should be returned with the additional entry 'w'.

def list_test(first_input, second_input, third_input):
    first_input.append('a')
    second_input += ['a','b','c']
    return third_input + ['w']
    pass # replace this line with your code



first_input = [1,2,3]
second_input = [4,5,6]
third_input = [7,8,9]

print list_test(first_input, second_input, third_input)
#>>> [7,8,9,'w']
print first_input
#>>> [1,2,3,'a']
print second_input
#>>> [4,5,6,'a','b','c']
print third_input
#>>> [7,8,9]

#---------------------8---------------
# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def is_equal_lists(a, b):
    n = len(a)
    while n:
        if a[-n] != b[-n]:
            return False
        n -= 1
    return True

def sort_by_columns(list_of_lists):
    res = []
    n = len(list_of_lists)
    while n:
        row = []
        for OneList in list_of_lists:
            row.append(OneList[-n])
        res.append(row)
        n -= 1
    return res

def symmetric(p):
    for el in p:
        if len(el) != len(p):
            return False
    q = sort_by_columns(p)
    n = len(p) 
    while n:
        if not is_equal_lists(p[-n], q[-n]):
            return False
        n -= 1
    return True
    

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False





    


    

