#!/bin/python3
"""
The code template that hackerrank provides has some code that is specific 
to there back end system, which throws errors when you try to run it locally.
"""
import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    result = len(set(s1).intersection(set(s2)))
    if result != 0:
        return "YES"
    elif result == 0:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

