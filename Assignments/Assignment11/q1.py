#1. Write a program which accepts one number and checks whether it is prime or not. 
#  Input: 11
#Output: Prime Number

def IsPrime(No):
    if No <= 1:
        return False
    for i in range(2,No):
        if No%i ==0:
            return False
    return True

def main():
    num=int(input("Enter the number: "))
    Result=IsPrime(num)

    if IsPrime(num):
        print("The number is prime number")
    else:
        print("The number is not prime number")\

if __name__=="__main__":
    main()