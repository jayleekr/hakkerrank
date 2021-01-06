#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    sealevel = 0
    vallleyNum = 0
    for char in path:
        if char == 'U' :
            sealevel = sealevel+1
            if sealevel == 0:
                vallleyNum = vallleyNum+1        
        else: # 'D'
            sealevel = sealevel-1
            
                
    return vallleyNum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
