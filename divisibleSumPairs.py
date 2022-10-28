import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))

def divisibleSumPairs(n, k, ar):
    counter = 0
    for i in range(n):
        for j in range(n):
            if (ar[i] + ar[j])%k == 0 and i<j:
                counter = counter + 1
    return counter

 print(divisibleSumPairs(n, k, ar))
         
