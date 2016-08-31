from __future__ import division
from math import log


def f(x):
    return 1/x

def f_a(x,h):
    return (log(x+h) - log(x))/h

def err(x,y):
    return abs(x-y)

h = 1
x = .25
maxError = 0
for i in range(1,40):
    h = .25*h
    approx = f_a(x,h)
    exact = f(x)
    error = err(exact,approx)
    print "h: %f    exact %f    approx %f   error %f" %(h,exact,approx,error)
    if error > maxError:
        maxError = error
print "i: %d Max Error: %.10f" % (i,maxError)




