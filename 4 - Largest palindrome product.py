def isPalindrome(x):
          
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        # x > 0
        y = x
        a = 1
            
        while (a * 10 < x):
            a *= 10
            
        while (x % 10 != x):
            
            if x % 10 != y // a:
                return False
                
            x //= 10
            y %= a
            a //= 10
            
        return True
# end def isPalindrome
        
factor_palindrome = []

for i in range (100, 999):
    for j in range (100, 999):
        if isPalindrome(i * j):
            factor_palindrome.append(i * j)

print ( max(factor_palindrome) )
            
