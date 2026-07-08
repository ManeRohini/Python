#5. Write a program which accepts one number from the user and checks whether the number is prime or not.
#Input: 5  Output: It is Prime Number

def is_prime(num):
    if num <= 1:          
         return False
    for i in range(2, int(num**0.5) + 1):   
        if num % i == 0:  
            return False
    return True
    
def main():
    no=int(input("Enter the value: "))
    check=is_prime(no)

    if(check==True):
        print("prime number")
    else:
        print("Not a prime number")
    
if __name__ =="__main__":
    main()