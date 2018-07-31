# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit 
# numbers.

palindromes=[]

def check_palindrome(a):
    
    # Function checks if input is a palindrome
    
    string_a = str(a)
    list_a = list(string_a)
    
    if (list_a) == (list_a[::-1]):     
        return ('is palindrome')
    else: 
        return ('not palindrome')

def largest_prod ():
    
    # This function will find products of 2-digit numbers, and check for 
    # Palindromes

    # nested for loops that checks if i * n is a palindrome, 

    for i in range(999,100,-1):
        for n in range(999,100,-1):
            prod = n*i
            
            if check_palindrome(prod) == 'is palindrome':
                palindromes.append(prod)
                

largest_prod()
print(max(palindromes))
