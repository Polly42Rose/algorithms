#!/bin/python3

from collections import Counter

# Complete the isValid function below.
def isValid(s):
    c = dict(Counter(list(s)))
    repet = dict()
    for key, value in c.items():
        if value not in repet:
            if len(repet) == 2:
                return "NO"
            if len(repet) == 1:
                repet[value] = 1
            else:
                repet[value] = 1
        else:
            repet[value] += 1
    k = list(repet.keys())
    v = list(repet.values())
    if len(k) == 2:
        if v[0] != 1 and v[1] != 1:
            return "NO"
        if k[0] != 1 and k[1] != 1 and (abs(k[0] - k[1]) > 1 or repet[max(k[0], k[1])] > 1) or (v[0] != 1 and v[1] != 1):
            return "NO"
        if k[0] == 1 or k[1] == 1 and repet[1] > 1:
            return "NO"
    return "YES"

if __name__ == '__main__':

    s = input()

    result = isValid(s)
    print(result)