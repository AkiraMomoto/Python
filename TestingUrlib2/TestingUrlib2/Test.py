import urllib2
import urllib

# URL = Uniform Resource Locater. The addresses of all files on the world wide web

# A request object, containing everything needed for an HTTP/1.1 request
wizardLink = urllib2.Request("https://wizard101.com")

# the status number of connection, whether it worked or not
print urllib2.urlopen(wizardLink).getcode()

# The meta information of the response
print urllib2.urlopen(wizardLink).info()

# returns URL. useful for checking for redirections
print urllib2.urlopen(wizardLink).geturl()

""" 
A Mapping object is any iterable 2 - element Array object. For instance: Dictionaries in python
"""
map = {'bob':34,'mary':54,'james':89}

""" 
    HTTP stands for Hyper Text Transfer Protocol, and handles how a message is sent to a server, how a server receives that message. Each HTTP Call is independent of one another
"""
# Transforms a map into a string of POST data usable by urlopen
print urllib.urlencode( map )

