x = 600851475143 

primes = [1]

while x != 1:
    for i in range (max(primes) + 1, x + 1):
        if x % i  == 0:
            primes.append(i)
            x = x // i
            break
    
print ( max( primes ) )
