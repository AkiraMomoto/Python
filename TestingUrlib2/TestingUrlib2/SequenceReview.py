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

d = {'foo': 'x',
    'bar': 'y',
    'zoo': None,
    'foobar': None}

# iterate over a copy of the dictionary, and replace none values wuth updated values
# print dict((k, 'updated') for k, v in d.iteritems() if v is None)

# Can it be done using filter?
# - No, Filter returns a SEQUENCE not a dictionary, and only takes one item
"""
    
    *************************************************************************************************************
    """
# Testing Web Connecting VIA Python
import urllib2
import urllib

# Send a request to receive the file, get the response and store it in a variable
request = urllib2.Request("http://api.researcher.poly.edu/test")
jsonTextPractice = urllib2.urlopen(request)

# The data is stored as a string, and has a tag that needs to be removed to become a JSon string
fileText = jsonTextPractice.read()

# Strip that tag from both sides, leave the list alone
fileText = fileText.strip("</pre>")

# Convert the string into the list represented
# This leaves me with a list of objects, or a dictionary
import ast

dictionaryList =  ast.literal_eval(fileText)

# Lets try making our own dictionary

jsonDic = {}

for item in dictionaryList:
    jsonDic = item


# now we can play with json since we have a fully working python dictionary
import json

# convert the dictionary into a json string
jsonString = json.dumps(jsonDic, sort_keys=True, indent=4, separators=(',', ': '))

print jsonString

