def is_prime(x):
    
    # check if the number is a negative 
    if x> 1:
        # you divide x with every number between 2 and x+1  and if its divisible return false 
        for i in range (2, x+1):
            # check only that x and 1  can divide x the users input 
            if x% i == 0 and i!=x and i !=1:
                return False 
        else:
            return True 
    else:
        
        return False                 
   
 
print (is_prime(17))

