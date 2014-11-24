#---1---
# Rabbits Multiplying

# A (slightly) more realistic model of rabbit multiplication than the Fibonacci
# model, would assume that rabbits eventually die. For this question, some
# rabbits die from month 6 onwards.
#
# Thus, we can model the number of rabbits as:
#
# rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
# rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
# For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2)
#
#
# For months > 5:
# All the rabbits that are over 5 months old die along with a few others
# so that the number that die is equal to the number alive 5 months ago.
# Before dying, the bunnies reproduce.
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
# This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...
#
# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)


cache = {} # start cache as an empty dictionary
def cached_execution(cache, proc, proc_input):
    # Your code here
    # cache = {'proc':{'key':val}}
    key = str(proc)[str(proc).find('function') + 9:]
    key = key[:key.find(' ')]
    print key
    if key in cache:
       if str(proc_input) in cache[key]:
            return cache[key][str(proc_input)]
    else:
        cache[key] = {}
    cache[key][str(proc_input)] = proc(proc_input)
    return cache[key][str(proc_input)]


def rabbits(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n >1:
        return rabbits(n-1)+rabbits(n-2)-rabbits(n-5)




print cached_execution(cache, rabbits, 30)
#>>> 35

s = ""
for i in range(1,31):
    s = s + str(cached_execution(cache, rabbits, i)) + " "
print s
#>>> 1 1 2 3 5 7 11 16 24 35 52

#----2----
# Spreading Udaciousness
 
# One of our modest goals is to teach everyone in the world to program and
# understand computer science. To estimate how long this will take we have
# developed a (very flawed!) model:

# Everyone answering this question will convince a number, spread, (input to 
# the model) of their friends to take the course next offering. This will 
# continue, so that all of the newly recruited students, as well as the original
# students, will convince spread of their
# friends to take the following offering of the course.
# recruited friends are unique, so there is no duplication among the newly
# recruited students. Define a procedure, hexes_to_udaciousness(n, spread,
# target), that takes three inputs: the starting number of Udacians, the spread
# rate (how many new friends each Udacian convinces to join each hexamester),
# and the target number, and outputs the number of hexamesters needed to reach 
# (or exceed) the target.

# For credit, your procedure must not use: while, for, or import math. 

def hexes_to_udaciousness(n, spread, target):
    if n < target:
        return 1 + hexes_to_udaciousness((n + n*spread), spread, target)
    return 0
        



# 0 more needed, since n already exceeds target
print hexes_to_udaciousness(100000, 2, 36230) 
#>>> 0

# after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
print hexes_to_udaciousness(50000, 2, 150000) 
#>>> 1 

# need to match or exceed the target
print hexes_to_udaciousness(50000, 2, 150001)
#>>> 2 

# only 12 hexamesters (2 years) to world domination!
print hexes_to_udaciousness(20000, 2, 7 * 10 ** 9) 
#>>> 12 

# more friends means faster world domination!
print hexes_to_udaciousness(15000, 3, 7 * 10 ** 9)
#>>> 10 


#---3---
# Deep Count 

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.

# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.


# For this procedure, you will need a way to test if a value is a list. We have
# provided a procedure, is_list(p) that does this:

def is_list(p):
    return isinstance(p, list)

# It is not necessary to understand how is_list works. It returns True if the
# input is a List, and returns False otherwise.

def deep_count(p):
    length =  len(p)
    for el in p:
      if is_list(el):
         length += deep_count(el)
    return length




print deep_count([1, 2, 3])
#>>> 3

# The empty list still counts as an element of the outer list
print deep_count([1, [], 3]) 
#>>> 3 

print deep_count([1, [1, 2, [3, 4]]])
#>>> 7

print deep_count([[[[[[[[1, 2, 3]]]]]]]])
#>>> 10

#---4---
#Feeling Lucky
 
#In Unit 6, we implemented a page ranking algorithm, but didn't finish the final
#step of using it to improve our search results. For this question, you will use
#the page rankings to produce the best output for a given query.

#Define a procedure, lucky_search, that takes as input an index, a ranks
#dictionary (the result of compute_ranks), and a keyword, and returns the one
#URL most likely to be the best site for that keyword. If the keyword does not
#appear in the index, lucky_search should return None.

def lucky_search(index, ranks, keyword):
    resPage = None
    bestRank = 0
    simpleSearch = lookup(index, keyword)
    if simpleSearch:
        for el in simpleSearch:
            if (el in ranks) and (ranks[el] > bestRank):
                resPage = el
                bestRank = ranks[el]
    return resPage
    
            

cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""",
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""",
}

def get_page(url):
    if url in cache:
        return cache[url]
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
    
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


#Here's an example of how your procedure should work on the test site: 

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)



print lucky_search(index, ranks, 'Hummus')
#>>> http://udacity.com/cs101x/urank/kathleen.html

print lucky_search(index, ranks, 'the')
#>>> http://udacity.com/cs101x/urank/nickel.html

print lucky_search(index, ranks, 'babaganoush')
#>>> None

#---5---
# Single Gold Star

# Family Trees

# In the lecture, we showed a recursive definition for your ancestors. For this
# question, your goal is to define a procedure that finds someone's ancestors,
# given a Dictionary that provides the parent relationships.

# Here's an example of an input Dictionary:

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

# Define a procedure, ancestors(genealogy, person), that takes as its first input
# a Dictionary in the form given above, and as its second input the name of a
# person. It should return a list giving all the known ancestors of the input
# person (this should be the empty list if there are none). The order of the list
# does not matter and duplicates will be ignored.

def ancestors(genealogy, person):
    res = []
    if person in genealogy:
        res+= genealogy[person]
        for parent in genealogy[person]:
            res+= ancestors(genealogy, parent)
    return res




# Here are some examples:

print ancestors(ada_family, 'Augusta Ada King')
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon','Captain John Byron']

print ancestors(ada_family, 'Judith Blunt-Lytton')
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron']

print ancestors(ada_family, 'Dave')
#>>> []

#---6---
# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def get_row(n):
    res = []
    if n < 1:
        return res
    if n == 1:
        res += [1]
    if n > 1:
        prevRow = get_row(n-1)
        for i in xrange((len(prevRow)- 1)):
          res.append(prevRow[i] + prevRow[i+1])
        res =  [1]+ res +[1]
    return res

def triangle(n):
    res=[]
    for i in xrange(n):
        res.append(get_row(i+1))
    return res


#For example:

print triangle(0)
#>>> []

print triangle(1)
#>>> [[1]]

print triangle(2)
#>> [[1], [1, 1]]

print triangle(3)

#>>> [[1], [1, 1], [1, 2, 1]]

print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]


#---7---
# Triple Gold Star

# Only A Little Lucky

# The Feeling Lucky question (from the regular homework) assumed it was enough
# to find the best-ranked page for a given query. For most queries, though, we
# don't just want the best page (according to the page ranking algorithm), we
# want a list of many pages that match the query, ordered from the most likely
# to be useful to the least likely.

# Your goal for this question is to define a procedure, ordered_search(index,
# ranks, keyword), that takes the same inputs as lucky_search from Question 5,
# but returns an ordered list of all the URLs that match the query.

# To order the pages, use the quicksort algorithm, invented by Sir Tony Hoare in
# 1959. Quicksort provides a way to sort any list of data, using an expected
# number of comparisons that scales as n log n where n is the number of elements
# in the list.

# The idea of quicksort is quite simple:

# If the list has zero or one elements, it is already sorted.

# Otherwise, pick a pivot element, and split the list into two partitions: one
# contains all the elements equal to or lower than the value of the pivot
# element, and the other contains all the elements that are greater than the
# pivot element. Recursively sort each of the sub-lists, and then return the
# result of concatenating the sorted left sub-list, the pivot element, and the
# sorted right sub-list.

# For simplicity, use the first element in the list as your pivot element (this
# is not usually a good choice, since it means if the input list is already
# nearly sorted, the actual work will be much worse than expected).

def lucky_search(index, ranks, keyword):
    resPage = None
    bestRank = 0
    simpleSearch = lookup(index, keyword)
    if simpleSearch:
        for el in simpleSearch:
            if (el in ranks) and (ranks[el] > bestRank):
                resPage = el
                bestRank = ranks[el]
    return resPage

def ordered_search(index, ranks, keyword):
    res_ranks = {}
    simpleSearch = lookup(index, keyword)
    if simpleSearch:
        for el in simpleSearch:
            if (el in ranks):
               res_ranks[el] = ranks[el]
    ol = get_sort_list_from_dict(res_ranks)
    return ol


def get_sort_list_from_dict(dict_with_ranks):
    rank_list= []
    ol = []
    for key in dict_with_ranks:
        rank_list.append(dict_with_ranks[key])
    sorted_list = my_qsort(rank_list)
    for el in sorted_list:
        for key in dict_with_ranks:
            if el == dict_with_ranks[key]:
                ol.append(key)
    return ol


def my_qsort(ul):
        if len(ul) == 0:
            return ul
        if len(ul) == 1:
            return ul
        pivot = ul[0]
        ul = ul[1:]
        leftPrt = []
        rightPrt = []
        for el in ul:
            if el > pivot:
               leftPrt.append(el)
            else:
               rightPrt.append(el)
        ol = my_qsort(leftPrt) + [pivot] + my_qsort(rightPrt)
        return ol   
        

cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""",
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""",
}

def get_page(url):
    if url in cache:
        return cache[url]
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


# Here are some example showing what ordered_search should do:

# Observe that the result list is sorted so the highest-ranking site is at the
# beginning of the list.

# Note: the intent of this question is for students to write their own sorting
# code, not to use the built-in sort procedure.

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)

print ordered_search(index, ranks, 'Hummus')
#>>> ['http://udacity.com/cs101x/urank/kathleen.html',
#    'http://udacity.com/cs101x/urank/nickel.html',
#    'http://udacity.com/cs101x/urank/arsenic.html',
#    'http://udacity.com/cs101x/urank/hummus.html',
#    'http://udacity.com/cs101x/urank/index.html']

print ordered_search(index, ranks, 'the')
#>>> ['http://udacity.com/cs101x/urank/nickel.html',
#    'http://udacity.com/cs101x/urank/arsenic.html',
#    'http://udacity.com/cs101x/urank/hummus.html',
#    'http://udacity.com/cs101x/urank/index.html']


print ordered_search(index, ranks, 'babaganoush')
#>>> None




