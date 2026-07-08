#2.Write a program which contains one function named as ChkNum() which accepts one parameter as number. 
# If number is even then it should display “Even number”, otherwise display “Odd number” on console.
#Input: 11  Output: Odd Number
#Input: 8  Output: Even Number

def Chknum(No):
    if(No%2==0 ):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    value=int(input("Enter the number: "))
    Chknum(value)

if __name__ =="__main__":
    main()