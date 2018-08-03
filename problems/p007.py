#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?
countprimes = 0

def is_prime(a):
    
    # function checks if input is prime
    
    prime_response = True
    
    for n in range (2,a):
       
        if a % n == 0:
            
            return False
        
    return True
                        
def find_primes(nth):
    
    # using the is_prime() function, this function loops to find primes
    # up to the intended range
    n = 2
    countprimes = 0
    
    while countprimes <= (nth-1):
            
        prime_response = is_prime(n)
        
        if prime_response == True:
    
#            print(n)
            countprimes += 1
            myprime = n
        n +=1
    
#   print("number of primes = ",countprimes)
    print("the {}th prime is = ".format(nth), myprime)


print("What number prime would you like to find ? Please input an integer")     
nth = int(input())
find_primes(nth)


