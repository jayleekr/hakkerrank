#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_max = None
    for i in range(4):
        for j in range(4):
            _sum_max= arr[i][j] + arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1] +arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum_max ==None or _sum_max > sum_max :
                sum_max = _sum_max
    return sum_max

_str="1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 2 4 4 0 0 0 0 2 0 0 0 0 1 2 4 0" 
_l=list(map(int,_str.split()))
input_list_2D=[]
for i in range(6):
    input_list_2D.append(_l[i*6:i*6+6])
print(input_list_2D)
print(str(hourglassSum(input_list_2D)))