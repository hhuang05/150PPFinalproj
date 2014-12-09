#!/usr/bin/env python

# Author: Moses Huang
# Created Date: 11/10/2014

PURPOSE = "Setup problem and derive the necessary matrices for downstream"
USAGE = "WRITE IN USAGE"

import sys
import numpy as np


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
    data = np.loadtxt(argv[1], delimiter=',', skiprows=1, usecols=(1,2,3,4,5,6))

    X = data[:, 0:5]
    Y = data[:, 5]
    w = [-1.731855, 2.980617, 2.698284, -3.591651, -3.714157]
    
    w_sol = np.linalg.lstsq(np.dot(X.T, X), np.dot(X.T,Y))[0]

    A = np.linalg.inv(np.dot(X.T, X))
    b = np.dot(X.T, Y)
    w_sol2 = np.dot(A,b)

    print w, np.linalg.norm(np.dot(X,w) - Y)
    print w_sol, np.linalg.norm(np.dot(X,w_sol) - Y)
    print w_sol2
    

    

if __name__ == '__main__':
    main(sys.argv)
