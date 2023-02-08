#!/bin/python3
for i in range(int(input())):
    n = int(input())
    sum_of_squares = (n*(n+1)*((2*n)+1))/6
    sum_of_n = ((n*(n+1))/2)**2
    print(int(abs(sum_of_squares - (sum_of_n))))
