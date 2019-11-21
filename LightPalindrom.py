import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    answ = 0
    for i, symb in enumerate(s):
        count = 1
        left = i - 1
        right = i + 1
        while left >= 0 and right < n:
            if s[left] == s[right]:
                if count == 1:
                    count += 1
                elif s[left + 1] == s[left] and s[right] == s[right - 1]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1
            else:
                break
        answ += count
        count = 0
        left = i
        right = i + 1
        while left >= 0 and right < n:
            if s[left] == s[right]:
                if count == 0:
                    count += 1
                elif s[left + 1] == s[left] and s[right] == s[right - 1]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1
            else:
                break
        answ += count
    return answ

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = substrCount(n, s)
    print(result)
