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
        """
            We want to access all tags and all data from the website's XML and read it into a python dictionary. Once in the dictionary we can pretty print it using json
            """
        # What does the XML page look like?
        
        # Found the root of the tree!
        tree = ET.ElementTree(resource)
    
        root = tree.getroot()
        for child_of_root in root:
            print child_of_root.tag, child_of_root.attrib
    else:
        print "Error with url, returned error code: %s" %( str(resource.getcode()) )
else:
    print "The given url is faulty and redirected you elsewhere"
