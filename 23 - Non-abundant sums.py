# -*- coding: utf-8 -*-
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""

def isAbundant(num):   
    
    def divideBySet(num, s):
        divided = True
        while divided:
            divided = False
            for i in s:
                if num % i == 0 and i != 1:
                    num = num // i
                    divided = True
        return num
    
    def getDivs(num, s):
        if len(s) > 1:
            num = divideBySet(num, s)
            
        if num != 1:
            for i in range(2, num):
                if not num % i:
                    s |= getDivs(num // i, s)
                    s |= getDivs(i, s)
                    s |= set([i, num // i])
                    
        return s

    s = sum(getDivs(num, set([1])))
    
    if s > num:
        return True
    else:
        return False
    
def isSumOfTwoAbundants(num, abs):
    for i in abs:
        if i >= num:
            return False
        if (num - i) in abs:
            return True

abs = [i for i in range(1, 28124) if isAbundant(i)]
candidates = [i for i in range(1, 28124) if not isSumOfTwoAbundants(i, abs)]

print(sum(candidates))
