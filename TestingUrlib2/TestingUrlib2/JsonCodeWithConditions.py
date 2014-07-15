# Let's begin with importing the file of data from the website
import urllib2

# retrieve the resource from the website
request = urllib2.Request("http://api.researcher.poly.edu/test")

jsonString = urllib2.urlopen( request )

# Check to see that the url was not redirected

if jsonString.geturl() != "http://api.researcher.poly.edu/test":
    print "Incorrect url given"
# Check to see the url request was successful
elif jsonString.getcode() != 200:
    print "Error retrieving source"
else:
    # Now we can do our Json coding since the file came through
    import json

    # The text from the resource file can be read as a string, or left as a file like obj
    jsonText = json.loads( jsonString.read().strip("</pre>") )

    # Transform the text back into pretty json format
    theString = json.dumps(jsonText, indent = 4, separators=(', ', ':'))
    print theString

