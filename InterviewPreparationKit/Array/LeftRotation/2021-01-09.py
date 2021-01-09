#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    for _ in range(d%len(a)):
        a_0=a[0]
        a.pop(0)
        a.append(a_0)
    return a

_a=list(map(int,"1 2 3 4 5".split()))
[1,2,3].pop()
print(rotLeft(_a,5))

