"""This function approximates the derivative of sin(x) at x = .5 and outputs the maximum error and the corresponding index"""
from __future__ import division
from math import sin,cos
n = 30
h = 1
x = .5
errMax = None
iMax = None

for i in range(0,30):
    h = .25*h
    y = (sin(x + h) - sin(x)) / h
    error = abs(cos(x) - y )
    print "%d       %.30f      %.30f      %.30f" % (i,h,y,error)
    if error > errMax:
        errMax = error
        iMax = i
print "i: %d        max Error: %.30f" % (iMax, errMax)


