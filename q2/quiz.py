from __future__ import division
import math
import statistics
import random

def mean(a):
    return sum(a)/len(a)

def variance(a,m):
    return sum(pow(x-m,2) for x in a)/(len(a))

def standardDev(v):
    return math.sqrt(v)

def altv(a,m):
    return (sum(pow(x,2) for x in a) - (len(a)*m*m) )/(len(a))

def error(x,y):
    return abs(x-y)

data = []
for i in range(0,20):
    data.append(random.uniform(0,200))

for x in data:
    print x

m = mean(data)

v = variance(data,m)

s = standardDev(v)

print "m: %f       v: %f       s: %f" %(m,v,s)

print "m: %f       v: %f       s: %f" %(statistics.mean(data),statistics.pvariance(data),statistics.pstdev(data))

print "va : %f"% altv(data,m)

print "error(va): %.30f        error(vairiance): %.30f"  %(error(altv(data,m),statistics.pvariance(data)) , error( variance(data,m),statistics.pvariance(data)))
