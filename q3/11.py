from __future__ import division
from math import sin,pi,sqrt

def s(n):
    if n == 2:
        return 1
    else:
        return s(n-1)/(2 + 2*sqrt(1 - s(n-1)))

def p(n):
    return pow(2,n)*sqrt(s(n+1))

for n in (range(2,21)):
    print "n: %d    s_n: %.30f      p_n %.30f" %(n,s(n), p(n))
