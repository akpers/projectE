"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def isprime(x):
    
    for i in range (2, x):
        if x % i == 0:
            return False
        
    return True
#end def isprime

prime = 2
prime_sum = 0

while prime < 2000000:
    prime_sum += prime
    i = prime + 1
    while not isprime(i):
        i += 1
    prime = i
    #print( prime, prime_sum )
    
print ( prime_sum )
