"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_py_triplet(a,b,c):
    
    if (a >= b or b >= c):
        return False
        
    if (a*a + b*b != c*c):
        return False
    
    return True
#end def is_py_triplet
    
for i in range (0, 1001):
    for j in range (i, 1001):
        for k in range (j, 1001):
            if (is_py_triplet(i, j, k) and i + j + k == 1000):
                print (i, j, k, i * j * k)
            