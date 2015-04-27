#!/usr/bin/env python

import os,sys,argparse

IN_STREAM = sys.stdin

wfPath = "./pipefile"
try:
    os.mkfifo(wfPath)
except OSError:
    pass
wp = open(wfPath, 'w')

for line in IN_STREAM:
    wp.write(line)
wp.close()

