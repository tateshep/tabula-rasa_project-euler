# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit 
# numbers.



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
       
    x = 999
    
    y = 999
     
    for i in range(99,999,1):
        print (x,y)
        
        for n in range(99,999,1):

            prod = x*y
            #print(prod)
            if check_palindrome(prod) == 'is palindrome':

                print('found largest palindrome, it is : ', prod)
                #return prod

            x += - 1
        
        y += - 1 
        
        if x < 0:
            break
        
largest_prod()