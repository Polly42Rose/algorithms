#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count_a = dict(Counter(list(a)))
    count_b = dict(Counter(list(b)))
    rem_count = 0
    for key, val in count_a.items():
        if key in count_b:
            count_b[key] = abs(count_b[key] - val)
        else:
            rem_count += val
    for key, val in count_b.items():
        rem_count += val
    return rem_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
