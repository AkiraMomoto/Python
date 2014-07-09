import urllib2


wizardLink = urllib2.Request("https://wizard101.com")

print urllib2.urlopen(wizardLink).info()