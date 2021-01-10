#!/bin/python3

import math
import os
import random
import re
import sys

def minimumSwaps(array):
    visited_dict = {}
    for i in range(len(array)):
        array[i] = array[i]-1
        visited_dict[i]=False
    count = 0
    is_ordered=False
    c=0
    start=0
    while is_ordered == False:
        for i in range(start,len(array)):
            if visited_dict[i] == True:
                if i == len(array)-1:
                    is_ordered = True
                    break
                continue
            if array[i] == i:
                visited_dict[i] = True
            else: # array[i] != i:
                temp= array[i]
                array[i], array[temp] = array[temp], array[i]
                visited_dict[temp] = True
                c = c + 1
                if array[i] == i:
                    visited_dict[array[i]] = True
                else:
                    start = i
                    break
            if i == len(array)-1:
                is_ordered = True
    return c

_array=list(map(int,"2 31 1 38 29 5 44 6 12 18 39 9 48 49 13 11 7 27 14 33 50 21 46 23 15 26 8 47 40 3 32 22 34 42 16 41 24 10 4 28 36 30 37 35 20 17 45 43 25 19".split()))

print(minimumSwaps(_array))