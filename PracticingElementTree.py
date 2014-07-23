# Levi Mollison
# Learning how to properly use the XML Tree module

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

# Let's begin by making our own element
root = etree.Element("root")

# Can append children to elements as you would ITEMS to a LIST
root.append( etree.Element("OneChild") )

# but an easier way to create children is to use a subele factory them. This is done with the subelement list which returns the desired child
# it looks like this: child = etree.SubElement(parent, child tag name)
child2 = etree.SubElement(root, "Child2")
child3 = etree.SubElement(root, "Child3")

# Now that the elements are created, you can pretty print the xml doc you made
# print  (etree.tostring( root) )

# elements are organized as closely to lists as possible. so many list functions work on xml trees
child = root[0]
# print child.tag

# print len(root)

# in order to go through the tree like a list, you need to turn it into a list
children = list(root)

#for element in children:
#   print element.tag

# You can also insert elements at certain places that you wish using root.insert
root.insert(0, etree.Element("Child0"))

start = root[:1]
end = root[-1:]

""" 
    print start[0].tag
print end[0].
"""

# There is more than just tags, there is also attribute manipulation
# attributes are stored like dictionaries in elements, and are used the same way
root = etree.Element("root", interesting="Totally")
print etree.tostring(root)

# can also set them in an already created element
root.set("hello","huhu")
# get searches the element for the desired attribute value
# print root.get("hello")

# can order , sort and search for attributes exactly like keys
# print sorted(root.keys())

# Accessing text
root.text = "TEXT"
# print root.text