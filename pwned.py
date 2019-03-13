import sys
import urllib2
import hashlib


if (len(sys.argv) == 2):
    password = sys.argv[1]
else:
    print "Usage: python pwned.py <password>"
    exit(-1)

hash = hashlib.sha1()
hash.update(password)
digest = hash.hexdigest().upper()

print digest

headers = { 'User-Agent' : 'pwned.py' }
apiurl = "https://api.pwnedpasswords.com/range/" + digest[:5] 

print apiurl
req = urllib2.Request(apiurl, None, headers)
contents = urllib2.urlopen(req).read()

found = False
for line in contents.splitlines():
    linehash =  line[:35]
    linenums = line[36:]

    if (linehash == digest[5:]):
        found = True
        print "Password has been found " + linenums + " times :("

if (not found):
    print "Password was not found :)"
