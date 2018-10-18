#!/usr/bin/env python

import sys
import re
import string
import csv
path = r'trumpas.csv'

content = []

with open(path,'r',encoding='utf_8') as f:
    for line in f:
        for token in line.split(','):
            m = re.search('@(\w+)', token)
            n = re.search('\#(\d+)', token)
            l = re.search('(http[s]?://)((?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', token)
            if not m:
                if not n:
                    if not l:
                        content.append(token)
               


#print ("Twitter Handles:")
#for handle in twitter_handles:
#    print ("@%s" % handle)

#print ("Hashtags:")
#for hashtag in hashtags:
#    print ("#%s" % hashtag)

#print ("URLs:")
#for url in urls:
#    print (url)

print ("content")
for con in content:
    print (con)
