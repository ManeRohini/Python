#3. Write a program which contains one function named as Add() which accepts two numbers from user and returns addition of those two numbers.
#Input: 11  5  Output: 16

def Add(No1,No2):
    Sum=No1+No2
    return Sum

def main():
    value1=int(input("Enter the 1st number: "))
    value2=int(input("Enter the 2nd number: "))
    Ret =Add(value1,value2)
    print("Addition is: ", Ret)
    

if __name__ =="__main__":
    main()