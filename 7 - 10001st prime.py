def isprime(x):
    for i in range (2, x):
        if x % i == 0:
            return False
    return True

prime = 2
count = 1
print( isprime(3) )


while count != 10001:
    i = prime + 1
    while not isprime(i):
        i += 1
    prime = i
    print (count, prime)
    count += 1

print (prime)