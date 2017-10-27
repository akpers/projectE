# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:17:56 2017

@author: a_konev
"""

a = 0
b = 1
sum = 0

while (b < 4000000):
    if (b % 2 == 0):
        sum += b
    b += a
    a = b - a
    
print (sum)
    