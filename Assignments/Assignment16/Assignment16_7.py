#7.Write a program which contains one function that accepts one number from the user and returns 
# True if the number is divisible by 5, otherwise returns False.
#Input: 8  Output: False
#Input: 25  Output: True

def DivBy5(no):
    if no%5==0:
        return True
    else:
        return False
    

def main():
    num=int(input("Enter the num: "))
    Ret=DivBy5(num)
    print(Ret)
    
if __name__ =="__main__":
    main()