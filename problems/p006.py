#The sum of the squares of the first ten natural numbers is,
#
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.




def sum_squares ():
    
    sumsquares = 0

    
    for n in range (1,101):
        
        a = n**2
        
        sumsquares += a
    return sumsquares  
    
        
sumsquares = sum_squares()
#print (sumsquares)
    

def square_of_sums ():
    
    squareofsums = 0
    a = []
    
    for n in range (1,101):
        
        a.append(n)
        
        
    squareofsums = sum(a)**2
    return squareofsums
        
    
squareofsums = square_of_sums ()


differenceofsums = squareofsums - sumsquares

print (differenceofsums)