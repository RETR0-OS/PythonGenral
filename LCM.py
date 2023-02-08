#!/bin/python3

import sys
from math import gcd

def find_num(n):
    num_list = [x for x in range(1,n+1)]
    lcm = 1
    for i in num_list:
        lcm = lcm*i//gcd(lcm,i)
    return(lcm)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_num(n))
