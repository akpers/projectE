# -*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz_length(n):
    count = 0
    initial = n
    while 1 != n:
        count += 1
        if 0 == n % 2:
            n //= 2
        else:
            n = 3*n + 1
    
    return initial, count

def collatz_gen(up_to_n):
    for i in range( 1, up_to_n + 1 ):
        yield collatz_length( i )

max_len = 0
index   = 0

for i in collatz_gen(1000000):
    if i[ 1 ] > max_len:
        index, max_len = i
        
print(index, max_len)