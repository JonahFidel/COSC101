# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# HW 11
# ----------------------------------------------------------
# Please answer these questions after having completed the 
# entire assignment.
# ----------------------------------------------------------
# Name: Jonah Fidel 
# Hours spent in total: 20
# Collaborators (if any) and resources used (if any):  Alex Indick, Edwin Amador, Compsci tutors
# This assignment tries to connect what you've learned in
# in this course with the real world, by guiding you the
# process of building a small but real web search engine. 
# What did you think of this assignment?
#   It was very satisfying to finish but frustrating to work through. 
# Feedback: What was the hardest part of this assignment?
#   random_surfer_simulation
# Feedback: Any suggestions for improving the assignment?   
#   more examples/guidance
# ---------------------------- ------------------------------

import urllib2
import random

def main():
    '''() -> None
    This is the main function which calls all other functions necessary for the search
    engine to run. 
    '''
    print "Welcome to my mini search engine!"
    reverse_index = {}                              # initialize dictionaries 
    web_graph = {}                      
    crawl_web('a.html', reverse_index, web_graph)                    # crawls the web (visits all linked pages) starting at the page 'a.html'
    page_ranks = random_surfer_simulation(web_graph, .15, 100000)    # simulates a web surfer visiting sites 100,000 times 
    search_engine(reverse_index, page_ranks)                         # call to prompt user for a search term 
    print 'The web graph is:', web_graph

def download_page(pagename):
    '''(str) -> str
    This function takes a string representing a web page as a parameter. It retrieves
    and returns the full contents of said web page as a string with linebreaks added.
    '''
    fullurl = "http://cs.colgate.edu/cosc101/testweb/" + pagename
    fulltext = ''
    fileobject = urllib2.urlopen(fullurl)
    for line in fileobject:
        fulltext += line + '\n'
    return fulltext

def extract_links(fulltext):
    '''(str) -> list 
    This function takes as a parameter the full text of a web page (a string), most likely
    obtained through the download_page function. From this string, the function extracts
    all links to other pages and returns them as a list.
    >>> extract_links('abc <a href="a.html">xyz</a>')
    ['a.html']
    >>> extract_links('abc <a blah="a.html">xyz</a>')
    []
    >>> extract_links('A <a href="one.html">B</a> C <a href="two.html">D</a>')
    ['one.html', 'two.html']
    ''' 
    links = []
    start = 0
    end = len(fulltext)
    marker = '<a href='
    while fulltext.find(marker, start, end) != -1:               
        start = fulltext.find(marker, start, end) + 1           # locates link markers 
        j = start + 8                                           # accounts for length of link marker ('<a href=')
        link = ""
        while fulltext[j] != '"':
            link += fulltext[j]
            j+=1
        links.append(link)                          # adds links to a list 
    return links
    
                
    
def remove_tags(fulltext):
    '''(str) -> str
    This function takes as a parameter the full text of a webpage (usually acquired via the function download_page)
    and returns the same text with HTML tags removed.
    >>> remove_tags('<b>abc</b>')
    'abc'
    >>> remove_tags('A<b>B</b>C')
    'ABC'
    >>> remove_tags('abc <a href="a.html">xyz</a>')
    'abc xyz'
    '''
    new_text = ''
    startmarker = '<'
    endmarker = '>' 
    new_startmarker = -1              # initializes variables as strings and ints for indexing 
    new_endmarker = -1
    startmarkers = []
    endmarkers = [] 
    fulltext_remaining = fulltext          # variable to keep track of how much text has been analyzed
    while '<' in fulltext_remaining:
        if '<' in fulltext:
            new_startmarker = fulltext.find(startmarker, new_startmarker + 1)     # finds the next marker starting at the previous marker
            startmarkers += [new_startmarker]                                    # adds marker to list 
            new_endmarker = fulltext.find(endmarker, new_endmarker + 1)
            endmarkers += [new_endmarker]
        fulltext_remaining = fulltext[endmarkers[-1]:-1]                         # truncates the text remaining
    new_text = fulltext[0:startmarkers[0]]
    for marker in range(len(startmarkers) - 1):
        new_text += fulltext[endmarkers[marker]+1:startmarkers[marker + 1]]       # string slices characters between the indicated markers 
    new_text += fulltext[endmarkers[-1] + 1:]
    return new_text

def normalize_word(string):
    '''(string) -> stringg letters are lower-cased.
    >>> normalize_word("That’s")
    'thats'
    >>> normalize_word('NONE!')
    'none'
    >>> normalize_word('Hello, goodBYE!')
    'hellogoodbye'
    '''
    new_string = ''
    for i in range(len(string)):                                 # searches for only alphabetical characters
        if string[i].isalpha():
            new_string += string[i]
    new_string = new_string.lower()
    return new_string

def index_page(pagename, fulltext, reverse_index):
    '''(str, str, dict) -> None
    This function accepts three parameters: a web page name, the full contents of that
    page as a string, and a Python dictionary storing the reverse index from that page.
    The function maps words to lists of web pages on which those words are found. 
    '''
    fulltext = remove_tags(fulltext)
    fulltext = fulltext.split()
    for word in fulltext:
        word = normalize_word(word)          # normalizes the entirity of fulltext
        if word != '':
            if word not in reverse_index:
                reverse_index[word] = [pagename]            # adds words from the current page to the reverse index 
            else:
                if pagename not in reverse_index[word]:
                   reverse_index[word].append(pagename)     
    return reverse_index
            
    

def crawl_web(seed_page, reverse_index, web_graph):
    '''(str, dict of str:list of str) -> None
    Crawls the web starting at the seed_page. Any
    page that can be reached from seeed_page by following links
    will be crawled.

    Each time a page is crawled, an entry is added to web_graph. the key is
    name of the page, the value is the list of links
    on that page. 
    '''
    if seed_page not in web_graph:
        text = download_page(seed_page)
        linked_pages = extract_links(text)           # creates a list of links on the current page
        web_graph[seed_page] = linked_pages
        reverse_index = index_page(seed_page, download_page(seed_page), reverse_index)   # adds the words from the current page to the reverse index
        for page in linked_pages:
            crawl_web(page, reverse_index, web_graph)

def random_surfer_simulation(web_graph, p, number_sims):
    '''(dict, int, int) -> None
    This function simulates thousands of random web searches across the web_graph. The function
    keeps a dictionary indicating how many times each page has been visited. This will be used
    later to compute the page ranks in the search engine. 
    ''' 
    visits = {}
    for page in web_graph:
        visits[page] = 0                                                # initialize number of visits to be zero 
    current_page = random.choice(web_graph.keys())                      # random page from web, prepeat number_sims times roll die
    for num in range(number_sims):                                                                                                             
        r = random.random()                                             # p will specify probability (between 0 and 1)
        if r <= p:
            current_page = random.choice(web_graph.keys())               # random page from web, bored, jumps to random spot in web
        else:
            current_page = random.choice(web_graph[current_page])        # random page from links on current page, clicks links on same page
        visits[current_page] += 1
    for key in visits.keys():
        visits[key] = visits[key]/float(number_sims)                    # divides digits by the total number of sims
    return visits                                                        

def list_union(list1, list2):
    '''(list, list) -> list
    This function takes two lists as parameters and creates a new list that contains all items found in either
    of the original lists, but eliminates duplicates.
    >>> list_union(['a.html', 'c.html'], ['a.html', 'b.html'])
    ['a.html', 'b.html', 'c.html']
    '''
    united_list = []         # initializes new list 
    for item in list2:
        if item not in united_list:
            united_list.append(item)
    for item in list1:
        if item not in united_list:
            united_list.append(item)
    return united_list

def list_intersection(list1, list2):
    '''(list, list) -> list
    This function accepts two lists and returns a new list that contains only those items
    that are found in both lists.
    >>> list_intersection(['a.html', 'c.html'], ['a.html', 'b.html'])
    ['a.html']
    '''
    list3 = []                # initialize new list
    for item in list1:
        if item in list2 and item not in list3:
            list3.append(item)
    return list3

def list_difference(list1, list2):
    ''' (list, list) -> list
    This function accepts two lists and returns a new list that contains only those items that are found in the
    first but not in the second list. 
    >>> list difference(['a.html', 'c.html'], ['a.html', 'b.html'])
    ['c.html']
    '''
    new_list = []                       # initialize new list 
    for item in list1:
        if item not in list2:
            new_list.append(item)
    return new_list 

def get_query_hits(word, reverse_index_dictionary):
    '''(str, dict) -> list 
    This function accepts a single search word and the reverse index dictionary. It returns a list
    of all the page names that match the search term.
    '''
    
    if word not in reverse_index_dictionary:
        return []                                   # if not in dictionary, return an empty list
    return reverse_index_dictionary[word]

def process_query(query, reverse_index):
    '''(str, dict) -> list
    This function accepts as parameters a query string and the reverse index dictionary. It
    returns a list of page names that match a given query. 
    '''
    terms = query.split()
    pos_terms = []
    neg_terms = []
    for term in terms:                                 #process positive terms and filter out negative ones
        if term.startswith('-'):
            neg_terms.append(normalize_word(term))
        else:
            pos_terms.append(normalize_word(term))
    if normalize_word(terms[0]) == 'and':      # searches for 'and' marker 
        pos_terms.pop(0)                       # removes 'and' from the search query in pos_terms 
        do_intersect = True                     # boolean variable 
    else:
        do_intersect = False
    matches = get_query_hits(pos_terms[0], reverse_index)      
    for term in pos_terms:
        term = normalize_word(term)
        hits = get_query_hits(term, reverse_index)          # returns hits for pos terms
        if do_intersect:
            matches = list_intersection(matches, hits)     # calculates matches 
        else:
            matches = list_union(matches, hits)
    for term in neg_terms:
        term = normalize_word(term)
        hits = get_query_hits(term, reverse_index)
        matches = list_difference(matches, hits)
    return matches

def print_ranked_results(matches, page_ranks):
    ''' (list, dict) -> None 
    The function takes in a list of query results and the page ranks dictionary as parameters
    print out the query results in ranked order, from highest to lowest rank.
    If no results should print that there are no matches
    '''
    if matches == []:
        print 'No matches for search terms'
    else:
        ranks = []
        for rank in page_ranks:
            if rank in matches:
                ranks.append((page_ranks[rank], rank))  # adds ranks and pagenames to a list of duples 
        ranks.sort()
        ranks.reverse()
        for rank in range(len(ranks)):
            print str(rank + 1) + ': ' + ranks[rank][1] + ' (rank: ' + str(ranks[rank][0]) + ')'   # prints the desired output of pagename: rank
            
def search_engine(reverse_index, page_ranks):
    '''(dict, dict) -> None
    This function prompts the user for a query and executes process_query and print_ranked_results
    for the given query. 
    '''
    end = False 
    while end == False:
        query = raw_input('Search terms? (enter "Done" to quit):')       # prompts user for query
        if query.lower() == 'done':
            end = True
            break
        matches = process_query(query, reverse_index)              # process the given query
        print_ranked_results(matches, page_ranks)                   # print the results of the given query

main()
