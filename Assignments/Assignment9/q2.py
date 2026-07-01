#2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.  
#Input: 10 20
#Output: 20 is greater

def ChkGreater(a,b):
    if a>b:
        return a
    else:
        return b
    

def main():
    No1=int(input("Enter 1st number: "))
    No2=int(input("Enter 2nd number: "))

    num=ChkGreater(No1,No2)
    print("The Greater number is: ",num)


if __name__ == "__main__":
    main()