# Levi Mollison
# NYU Poly 0525716


# First we need to obtain the data from some random site. It should come in as XML data
import urllib2

request = urllib2.Request("http://pokemondb.net/about")

resource = urllib2.urlopen(request)

# Now run the tests to make sure everything ran smoothly
if resource.geturl() == "http://pokemondb.net/about":
    if resource.getcode() == 200:
        # Now lets turn the data into a readable element tree to model the XML
        # Rename the module as ET for easier accessing purposes
        
        import xml.etree.ElementTree as ET
        # To get the root of the file, there are a few steps we need to go through
        # Get an iterable, turn it into an iterator and then we can get the root
        context = ET.iterparse(resource, events=("start", "end"))

        # turn it into an iterator
        context = iter(context)

        # get the root element
        event, root = context.next()
        ET.dump(root)
    else:
        print "Error with url, returned error code: %s" %( str(resource.getcode()) )
else:
    print "The given url is faulty and redirected you elsewhere"
