from operator import itemgetter
import random


def isLeft(a, b, c):
    return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])) > 0

def jarvis(S):
    P = []
    pointOnHull =  min(S, key=itemgetter(0))  # point with the lowest X, left-most point
    i = 0
    while True:
        P.append(pointOnHull)
        endpoint = S[0]
        for j in range(len(S)):
            if (endpoint == pointOnHull) or isLeft(S[j], endpoint, P[i]):  # cross product
                endpoint = S[j]
        i += 1
        pointOnHull = endpoint
        if endpoint == P[0]:
            break
    P.append(P[0])
    return P
