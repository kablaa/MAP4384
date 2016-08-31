from __future__ import division
from math import exp

def err(exact,approx):
    return abs(exact-approx)


def approx(n):
    return pow(1 + (1/n) ,n)

for i in range(0,41):
    n = pow(8,i)
    print " i: %d  exact: %.30f       approx: %.30f         error: %.30f" % ( i,exp(1), approx(n) , err(exp(1),approx(n)) )
