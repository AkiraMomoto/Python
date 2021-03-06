# Levi Mollison
# NYU Poly 0525716

try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5, this is the python we currently are running
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")

# First we need to obtain the data from some random site. It should come in as XML data
import urllib2


request = "http://lxml.de/lxmlhtml.html"

resource = urllib2.urlopen(request)

# Now run the tests to make sure everything ran smoothly
if resource.geturl() == "http://lxml.de/lxmlhtml.html":
    if resource.getcode() == 200:
        # Now lets turn the data into a readable element tree to model the XML
        # Rename the module as ET for easier accessing purposes
        
        
        """
            We want to access all tags and all data from the website's XML and read it into a python dictionary. Once in the dictionary we can pretty print it using json
            """
        root = etree.parse(resource).getroot()
        print root
        print "/n"
    # now its time to go through the xml and store it in a python dictionary
    # WE ARE ITERATING OVER THE XML DOCUMENT AND GETTING INFO! YESSS
        for element in root.iter():
            print("%s - %s, attribute: %s" % (element.tag, element.text, element.attrib))
    
    else:
        print "Error with url, returned error code: %s" %( str(resource.getcode()) )
else:
    print "The given url is faulty and redirected you elsewhere"
