def isprime(x):
    
    for i in range (2, x):
        if x % i == 0:
            return False
        
    return True
#end def isprime

prime = 2
count = 1

while count != 10001:
    i = prime + 1
    while not isprime(i):
        i += 1
    prime = i
    count += 1

print (prime)
