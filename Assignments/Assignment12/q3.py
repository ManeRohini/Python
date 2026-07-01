#3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def Calculations(No1,No2):
    Addition =No1+No2
    print("Addition is: ",Addition)
    subtraction =No1-No2
    print("Subtraction is: ",subtraction)
    multiplication =No1*No2
    print("Multiplication is: ",multiplication)
    Division =No1/No2
    print("Division is: ",Division)


def main():
    Num1=int(input("Enter 1st number: "))
    Num2=int(input("Enter 2nd number: "))

    Calculations(Num1,Num2)

if __name__ =="__main__":
    main()