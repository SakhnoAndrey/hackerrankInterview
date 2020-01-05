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

twoStrings()
