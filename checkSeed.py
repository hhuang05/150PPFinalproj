#!/usr/bin/env python

# Author: Moses Huang
# Created Date: 

PURPOSE = "WRITE IN PURPOSE"
USAGE = "WRITE IN USAGE"

import sys
import shlex
import subprocess as sp
import argparse

def main(argv):
    #cmdLineObj = includeParsing()
    for i in xrange(0, 40):
        cmd = "church -t -a " + argv[1] + " " + argv[2] 
        tokenized = shlex.split(cmd)
        p = sp.Popen(tokenized, stdout=sp.PIPE)
        out, err = p.communicate()
        print out


if __name__ == '__main__':
    main(sys.argv)
