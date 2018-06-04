#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    a1=0
    b1=0
    for i in range(3):
        if a[i]>b[i]:
            a1=a1+1
        elif a[i]<b[i]:
            b1=b1+1
    x=[]
    x.append(str(a1))
    x.append(str(b1))

    return x
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
