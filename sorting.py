import math
import os
import random
import re
import sys


def countSwaps():
    # Input CountSwaps
    s = "3 2 1"
    a = list(map(int, s.rstrip().split()))
    n = len(a)

    # Function CountSwaps
    count = 0
    for _ in range(n):
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                count += 1
    print("Array is sorted in {0} swaps.".format(str(count)))
    print("First Element: {0}".format(str(a[0])))
    print("Last Element: {0}".format(str(a[-1])))

def maximumToys():
    # Input maximum toys
    k = 50
    s = "1 12 5 111 200 1000 10"
    prices = list(map(int, s.rstrip().split()))

    # Function maximum toys
    count_max = 0
    basket = 0
    prices.sort()
    print(prices)
    for p in prices:
        if basket + p < k:
            basket += p
            count_max += 1
        else:
            break
    print(count_max)
    return count_max


maximumToys()
