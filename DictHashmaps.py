#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Dictionaries and Hashmaps

def checkMagazine():
    # input magazine and note
    m = 7
    n = 4
    str_magazine = "ive got a lovely bunch of coconuts"
    str_note = "ive got some coconuts"
    magazine = str_magazine.rstrip().split()
    note = str_note.rstrip().split()

    # function checkMagazine
    print("Yes" if Counter(note) - Counter(magazine) == {} else "No")


def twoStrings():
    # Input strings
    s1 = "hello"
    s2 = "world"

    # function twoStrings
    check = False
    for char in s1:
        if char in s2:
            check = True
            break
    return "YES" if check else "NO"


def sherlockAndAnagrams():
    # Input sherlockAndAnagrams
    s = "ifailuhkqq"

    # Function sherlockAndAnagrams
    dict = {}
    count = 0
    l = len(s)
    for i in range(l):
        for j in range(i, l):
            test = list(s[i:j + 1].strip())
            test.sort()
            sort = ''.join(test)
            if sort in dict:
                count += dict[sort]
                dict[sort] += 1
            else:
                dict[sort] = 1
    return count


def countTriplets():
    # Input countTriplets
    s = "1 3 9 9 81 243"
    r = 3
    arr = list(map(int, s.rstrip().split()))

    # Function countTriplets
    # set_arr = set(arr)
    if len(arr) <= 2:
        return 0
    map_arr = {}
    map_doubles = {}
    count = 0
    # Traversing the array from rear, helps avoid division
    for x in arr[::-1]:
        r_x = r * x
        r_r_x = r * r_x

        # case: x is the first element (x, x*r, x*r*r)
        count += map_doubles.get((r_x, r_r_x), 0)

        # case: x is the second element (x/r, x, x*r)
        map_doubles[(x, r_x)] = map_doubles.get((x, r_x), 0) + map_arr.get(r_x, 0)

        # case: x is the third element (x/(r*r), x/r, x)
        map_arr[x] = map_arr.get(x, 0) + 1
    return count


def freqQuery():
    # Input freqQuery
    queries = []
    print(os.path.dirname(__file__) + "/Data/freqQuery.txt")
    with open(os.path.dirname(__file__) + "//Data//freqQuery.txt") as f:
        for line in f:
            queries.append([int(x) for x in line.split()])

    # Function freqQuery
    value_dict = {}
    freq_dict = {}
    data_output = []
    for command, value in queries:
        freq = value_dict.get(value, 0)
        if command == 1:
            freq += 1
            value_dict[value] = freq
            freq_dict[freq] = freq_dict.get(freq, 0) + 1
            if freq - 1 > 0:
                freq_dict[freq - 1] = freq_dict.get(freq - 1, 0) - 1
        elif command == 2 and freq > 0:
            freq -= 1
            value_dict[value] = freq
            freq_dict[freq] = freq_dict.get(freq, 0) + 1
            freq_dict[freq + 1] = freq_dict.get(freq + 1, 0) - 1
        elif command == 3:
            data_output.append(1 if freq_dict.get(value, 0) > 0 else 0)
    return data_output


freqQuery()
