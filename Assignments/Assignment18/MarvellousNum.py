# This is a user defined module used in Assignment18_5.py

def ListAddOnlyPrime(lst):
    total = 0
    for i in lst: 
        
        prime = is_prime(i)                
        if prime == True :
            total += i  
        
        """""another way
        if is_prime(i):
            total +=i
        """""  
    return total


def is_prime(num):
    if num <= 1:          
         return False
    for i in range(2, int(num**0.5) + 1):   
        if num % i == 0:  
            return False
    return True