#!/usr/bin/env python

# Author: Moses Huang
# Created Date: 

PURPOSE = "WRITE IN PURPOSE"
USAGE = "WRITE IN USAGE"

import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt

def includeParsing():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    return args

def main(argv):
    # cmdLineObj = includeParsing()
    # DEFINE MAIN FUNCTIONS HERE
    data = np.loadtxt(argv[1])
    fig = plt.figure()
    ax = plt.gca()
    ax.scatter(data[:,0], data[:,1])
    #ax.set_xscale('log')
    #ax.set_yscale('log')
    ax.set_xlim(-100,100)
    ax.set_ylim(-100,100)
    plt.savefig(argv[2] + ".eps", bbox_inches='tight', format='eps', dpi=1200)


if __name__ == '__main__':
    main(sys.argv)
