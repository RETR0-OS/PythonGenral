#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prime_factors = []
    for i in range(1,n+1):
        #print(n%i)
        if n%i ==0:
            prime = True
            for x in range(2,i):
                #print(f"i is {i} and x is {x}")
                #print(i%x)
                if i%x==0:
                    prime =False
                    break
            if prime == True:
                prime_factors.append(i)
    print(max(prime_factors))
                    
