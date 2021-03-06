#!/bin/python3

import math
import os
import random
import re
import sys


# Warm-up Challenges

# Complete the sockMerchant function below.
def sockMerchant():
    # input sockMerchant(n, ar)
    n = int(9)
    s = "10 20 20 10 10 30 50 10 20"
    ar = list(map(int, s.rstrip().split()))

    # function sockMerchant(n, ar)
    d = {ar[0]: 0}
    for i in range(0, n):
        if ar[i] in d:
            d[ar[i]] += 1
        else:
            d[ar[i]] = 1
    number_pair = 0
    for k in d:
        number_pair += d[k] // 2
    return number_pair


def countingValleys():
    # input countingValleys(n, s)
    n = 8
    s = 'UDDDUDUU'

    # function countingValleys
    down_up = {'D': -1, 'U': 1}
    h = 0
    v = 0
    for symb in s:
        if h == 0 and symb == 'D':
            v += 1
        # h = h + 1 if symb == 'U' else h - 1
        h += down_up[symb]
    return v


def jumpingOnClouds():
    # input jumpingOnClouds
    n = int(6)
    s = "0 0 0 0 1 0"
    c = list(map(int, s.rstrip().split()))

    # fucntion jumpingOnClouds
    n = len(c)
    position = 0
    min_num = 0
    while position < n - 1:
        if position + 2 < n:
            position = position + 2 if c[position + 2] == 0 else position + 1
        else:
            position += 1
        min_num += 1
    return min_num


def repeatedString():
    # input repeatedString(s, n):
    s = "a"
    n = 1000000000000

    # function repeatedString
    k_full_string = n // len(s)
    k_el_end_str = n % len(s)
    count_a = k_full_string * s.count('a') + s[:k_el_end_str].count('a')
    return count_a

repeatedString()
