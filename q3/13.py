from __future__ import division
import numpy
from math import sqrt

#here we are getting the h values for each coresponding x value
def h(x):
    return sqrt(1-pow(x,2))

#here, we are getting the values of x_n. So the interval [0,1] divided into n peices
def xArr(N):
    result = []
    for k in range(0,N+1):
        result.append(k/(N))
    return result

#this is the formula for the area of a trapezoid
def area(a,b,h):
    return (a+b)*h/2

def trap(N):
    heights = []
    xx = xArr(N)
    for x in xx:
        heights.append(h(x))
    result = 0
#summing up the areas of all of the trapezoids
    for i in range(0,N):
        result = result + area(heights[i],heights[i+1],1/N)
    return result

#since trap() only calculates 1/4th of the area of the unit cricle, we need to muliply the result by 4
#this is a very bad approximation
print 4*trap(100000)


