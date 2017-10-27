def primes(x):
    i = 2
    result = list()
   
    while x % i != x:
        if x % i == 0:
            result.append(i)
            x //= i
        else:
            i += 1
           
    return result
# end def primes

num = 20
result = 1

for i in range (1, num + 1 ):
    temp = result
    for j in primes(i):
        if temp % j != 0:
            result *= j
        else:
            temp //= j
           
print (result)
