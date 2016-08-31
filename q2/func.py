from __future__ import division
import math
import random

def myFunc(a):
    n = len(a)
    n2 = math.floor(n/2)
    s1 = sum(a[0:int(n2)])
    s2 = sum(a[int(n2):n])/(n-int(n2))
    return (s1,s2)

def talor()

elems = []
for i in range(0,20):
    elems.append(random.uniform(0,100))

print elems
print myFunc(elems)




