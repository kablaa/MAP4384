from math import exp

numVals =20

def recursiveP(n):
    if n <= 0:
        return 1
    else:

        return exp(1) - (n+1)*recursiveP(n-1)

def alt(n):
    p = 1.0
    for i in range(1,n+1):
        print "%.30f - %d * %.30f = %.30f" % (exp(1), (i+1) , p ,exp(1) - (i+1)*p)
        p = exp(1) - (i+1)*p
    return p

alt(20)


