#!/bin/python3

import math
import os
import random
import re
import sys


# Arrays

# 2D Array - DS
def hourglassSum():
    # input hourglassSum
    arr = []
    with open("hourglasssum.txt") as f:
        for line in f:
            arr.append([int(x) for x in line.split()])

    # function hourglassSum
    max_hourglass = -9 * 7
    for i in range(4):
        for j in range(4):
            el = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] \
                 + arr[i + 1][j + 1] \
                 + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            max_hourglass = max(el, max_hourglass)
    return max_hourglass


# Arrays: Left Rotation
def rotLeft():
    # input rotLeft
    str_nd = "15 13"
    str_a = "33 47 70 37 8 53 13 93 71 72 51 100 60 87 97"
    nd = str_nd.split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, str_a.rstrip().split()))

    # fucntion rotLeft
    n = len(a)
    d_new = d % n
    a_new = a[d_new:] + a[:d_new]
    # str_new = ' '.join(str(i) for i in a_new)
    return a_new


# New Year Chaos
def inputMinimumBribes():
    # input minimumBribes
    t = 2
    n = 8
    q = "5 1 2 3 7 8 6 4"
    q = list(map(int, q.rstrip().split()))
    minimumBribes(q)
    n = 8
    q = "1 2 5 3 7 8 6 4"
    q = list(map(int, q.rstrip().split()))
    minimumBribes(q)


def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if i < q[i] - 3:
            print("Too chaotic")
            return
        for x in q[max(0, q[i]-2):i]:
            if x > q[i]:
                bribes += 1
    print(bribes)


# Minimum Swaps 2
def minimumSwaps():
    # input minimumSwaps
    n = 7
    str_arr = "1 3 5 2 4 6 7"
    arr = list(map(int, str_arr.rstrip().split()))

    # function minimumSwaps
    number = 0
    for i in range(n):
        while arr[i] != i + 1:
            tmp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = tmp
            number += 1
    return number

# Array Manipulation
def arrayManipulation():
    # input array manipulation
    n = 5
    m = 3
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

    # function array manipulation
    arr = [0] * n
    for x in queries:
        arr[x[0]-1] += x[2]
        if x[1] != n:
            arr[x[1]] -= x[2]
    sum_el = 0
    max_el = 0
    for x in arr:
        sum_el += x
        max_el = max(max_el, sum_el)
    return max_el


arrayManipulation()

