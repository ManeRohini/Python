"""
3. Write a program which accepts one number from the user and returns its factorial.
Input: 5  Output: 120

"""
def Factorial(No):
    fact=1
    for i in range(1,No+1):
        fact=fact*i
        
    return fact
    

def main():
    num=int(input("Enter the value: "))
    ret=Factorial(num)
    print(f"Factorial of {num} is: ",ret)
    
if __name__ =="__main__":
    main()