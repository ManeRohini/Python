#6.Write a program which accepts a number from the user and checks whether that number is positive, negative, or zero.
#Input: 11  Output: Positive Number
#Input: -8  Output: Negative Number
#Input: 0  Output: Zero

def Check(No):
    if No>0:
        print("Positive number")
    elif No<0:
        print("Negative number")
    else:
        print("zero")
    
def main():
    num=int(input("Enter the value: "))
    Check(num)
    
if __name__ =="__main__":
    main()