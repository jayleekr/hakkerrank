#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    def minCount(i): # i == index of list
        if i == 1:
            return 1
        if i == 0:
            return 0
        
        if c[i-2] == 0:
            return minCount(i-2) + 1
        else: # c[i-2] == 1:
            return minCount(i-1) +1
    return minCount(len(c)-1)


inputs="0 0 1 0 0 1 0"
c = list(map(int, inputs.split()))
jumpingOnClouds(c)

