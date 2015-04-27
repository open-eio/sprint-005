#!/usr/bin/env python

import os,sys,argparse

rfPath="./pipefile"
rp=open(rfPath,'r')
response=rp.read()
splitResponse=response.split("\n")
#print ("{"),
sys.stdout.write('{')
index=0
iMax=len(splitResponse)
i=0
while (i<(iMax-1)):
    #print index
    index=index+1
    sys.stdout.write(splitResponse[i])
    if (i<(iMax-2)):
        sys.stdout.write(",")
    i=i+1
sys.stdout.write("}")
#print "1: %s" % splitResponse[0]
#print "2: %s" % splitResponse[1]
rp.close()
#print "yeah"
#print rp
