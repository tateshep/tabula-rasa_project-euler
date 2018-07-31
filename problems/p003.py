# The prime factors of 13195 are 5, 7, 13 and 29.
#
#  What is the largest prime factor of the number 600851475143 ?

import math

factors = []
myprimelist=[]


def myfactors(a):
    
    #function to factor an input 'a'
    end = math.ceil(math.sqrt(a))
    
    for i in range(1, end):
        if a % i == 0:
            factors.append(i)
            
    return factors

def checkprime(a):
    
    x = False
    

#     function for finding if input is prime
#     Returns x =  False, if 'a' has a factor and therefore is not prime
#     x = True , if prime  because looped through without finding factor

    
    for i in range(2,(a),1):
                
        if a % i == 0:
            x = False
            return x 
        
        x = True 
    return x 
            
def myprimes():
    
    # This function grabs primes from list of factors
    
    for n in range(0,len(factors)):
                
        if checkprime(factors[n]) == True :
            
            myprimelist.append(factors[n])


myfactors(600851475143)
myprimes()
print(max(myprimelist))
