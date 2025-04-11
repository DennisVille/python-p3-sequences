#!/usr/bin/env python3

def print_fibonacci(length):
    n = length 
    a,b = 0,1
    fib_list = []
    for _ in range(n):
        fib_list.append(a)
        a,b = b, a + b
    print(fib_list)