# The prime factors of 13195 are 5, 7, 13 and 29.
#
#  What is the largest prime factor of the number 600851475143 ?



def myfactors(a):
    
    #function to factor an input 'a'
    
    factoring = True
    factors = []
    i = [1,2,3,4,5,6,7,8,9]
    
    while factoring == True:
        for n in i:
     
            if a % i[n] ==0:
                a =  a/i[n]
                factors.append(a)
            else:
                factoring = False
            print (factors)

def checkprime(a):
    
    # function for finding if input is prime
    pass

myfactors(100)