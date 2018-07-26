
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def find_multiples_sum(a):
    
    # list all natural numbers below 10 that are multiples of 3 or 5
    mynums = list(range(0,(a+1),1))
    print (mynums)
    
    # sum the above multiples

    
find_multiples_sum(10)