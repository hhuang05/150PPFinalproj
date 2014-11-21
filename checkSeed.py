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
    for i in xrange(120, 150):
        cmd = "church -s " + str(i) + " prob1.church"
        tokenized = shlex.split(cmd)
        p = sp.Popen(tokenized, stdout=sp.PIPE)
        out, err = p.communicate()
        print "seed:", i, out


if __name__ == '__main__':
    main(sys.argv)
