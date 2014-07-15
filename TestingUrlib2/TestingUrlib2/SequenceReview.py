"""
    Levi Mollison
    Review of Dictionaries, Lists and List Comprehension
"""
# Keys can be any immutable data type
dic = {"george":1, "bob":2, (3,4,5):"what", 56:"yea okay"}

# print dic.keys()

# Can build dictionaries with the dict constructor, which takes a list of key value paired Tuples
dic2 = dict( [ ("Georgey", 2), ("Bobby", 3), (  (3,4,5,) , 56 ) ] )

# print dic2.keys()

# Can create dictionaries with string names easily with dict
dic3 = dict( george=45, bob=56 )

# print dic3.keys()

#List Comprehension and filter practice

# Filter returns a sequence containings items from the sequence for which function(item) is true

def not_divisble_by_2_or_3(x):
    return x % 2 != 0 and x % 3 != 0;

# print filter(not_divisble_by_2_or_3, range(2, 25))

# What does Filtering none do?
str_list = [
        "I have stuff",
        "My partner, on the other hand",
        "Will not, MUAHAHAHAA",
        ""
]

# Filtering none does not let any values with str of length zero pass through.
str_list = filter(None, str_list)

# filtering other data types with None does not let ther uninitialized versions go through, or empty versions.
list_of_lists = [
            [1,2,3,4],
            [4,5,6,7],
            [],
            [4,8,5,32]
]

list_of_lists = filter(None, list_of_lists)

print list_of_lists

d = {'foo': 'x',
    'bar': 'y',
    'zoo': None,
    'foobar': None}

# iterate over a copy of the dictionary, and replace none values wuth updated values
# print dict((k, 'updated') for k, v in d.iteritems() if v is None)

# Can it be done using filter?
# - No, Filter returns a SEQUENCE not a dictionary, and only takes one item at a time
"""
    
    *************************************************************************************************************
    """
# Testing Web Connecting VIA Python
import urllib2

# now we can play with json since we have a fully working python dictionary
import json

# Send a request to receive the file, get the response and store it in a variable
request = urllib2.Request("http://api.researcher.poly.edu/test")

# Json.loads takes in a string ( rather than a file like object) and converts it into a Python object for python into unicode
jsonTextPractice = json.loads( urllib2.urlopen(request).read().strip("</pre>") )

""" # The data is stored as a string, and has a tag that needs to be removed to become a JSon string
fileText = jsonTextPractice.read()

# Strip that tag from both sides, leave the list alone
fileText = fileText.strip("</pre>")


# Convert the string into the list represented
# This leaves me with a list of objects, or a dictionary
import ast

dictionaryList =  ast.literal_eval(fileText)
"""

# convert the dictionary into a json string
jsonString = json.dumps(jsonTextPractice, sort_keys=True, indent=4, separators=(',', ': '))

print jsonString

