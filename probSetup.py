#!/usr/bin/env python

# Author: Moses Huang
# Created Date: 11/10/2014

PURPOSE = "Setup problem and derive the necessary matrices for downstream"
USAGE = "WRITE IN USAGE"

import sys
import subprocess
import argparse
import numpy as np
import random

"""
def includeParsing():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    return args
"""
def arrayToStdout(data, headerTxt):
    """  arrayToStdout :: ndarray
    Purely side-effects, writes ndarray to std out
    """
    np.savetxt(sys.stdout, data, fmt='%1.5f', delimiter=',',header=headerTxt)

def wishart_std(dof):
    """  wishart :: int -> ndarray -> ndarray  
    Generates a standard wishart distribution from input degree of freedom and a covariance matrix
    """
    U = np.triu(np.random.normal(size=(dof, dof)))
    cs = np.ravel([ np.random.chisquare(dof - i + 1, 1) 
                    for i in xrange(1, dof+1) ])
    indices = np.diag_indices(dof)
    U[indices] = cs
    return np.dot(U.T, U)
    

def sampleMVN(mu, sigma):
    """  sampleMVN :: ndarray -> ndarray -> ndarray  
    Samples a Multivariate normal given a vector of mean and covariance
    """
    N = sigma.shape[0]
    return np.random.multivariate_normal(mu, sigma, size=1)

def main(argv):
    dof = 5
    sigma_prior = wishart_std(dof)
    arrayToStdout(np.linalg.inv(sigma_prior), "")

if __name__ == '__main__':
    main(sys.argv)
