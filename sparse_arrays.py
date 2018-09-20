#!/bin/python
"""
The code template that hackerrank provides has some code that is specific 
to there back end system, which throws errors when you try to run it locally.
"""
import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    queryresult = []
    for x in range(len(queries)):
        count = 0
        for val in strings:
            if queries[x]== val:
                count += 1
        queryresult.append(count)
    return queryresult

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(raw_input())

    strings = []

    for _ in xrange(strings_count):
        strings_item = raw_input()
        strings.append(strings_item)

    queries_count = int(raw_input())

    queries = []

    for _ in xrange(queries_count):
        queries_item = raw_input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
