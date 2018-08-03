# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

def my_divide ():
    
    check= False
    a = 1
    checklist = []
    
    while check == False:
        
        for n in range (1,20,1):

            if a % n != 0:
                checklist = []
                a += 1
                
                
        if a % n == 0:
            
            checklist.append(0)
            #print(checklist)
            
            if len(checklist) == 20:
                
                print(a)
                check = True
                
        
            
            
            
            
my_divide()