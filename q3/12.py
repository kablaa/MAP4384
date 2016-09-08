from __future__ import division
from math import sin,pi,sqrt

def theta(n):
    return 2*pi/pow(2,n)

def f(n):
    if n ==2:
        return 1
    else:
        return f(n-1)/sqrt(2*(1+sqrt(1 - pow(f(n-1),2))))

def p(n):
    return pow(2,n-1)*f(n)


for n in range(3,21):
    print "n: %d    sin(theta_n): %.30f     p_n: %.30f" % (n,f(n),p(n))
