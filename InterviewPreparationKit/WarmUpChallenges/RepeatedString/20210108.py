#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    count_a_InS=0
    for c in s:
        if c == 'a':
            count_a_InS = count_a_InS + 1

    totalCount=0
    quotient=n//len(s)
    totalCount = count_a_InS * quotient
    
    remainder=n%len(s)
    if remainder > 0:
        for i,c in enumerate(s):
            if c == 'a':
                totalCount = totalCount + 1    
            if i == remainder - 1:
                break
    return totalCount    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
