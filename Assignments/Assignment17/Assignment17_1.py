"""""
1. Create one module named as Arithmetic which contains 4 functions as

Add() for addition

Sub() for subtraction

Mult() for multiplication

Div() for division

All functions accept two parameters as numbers and perform the operation.
Write a Python program which calls all the functions from the Arithmetic module by accepting the parameters from the user.

"""
import  ArithmaticModule

def main():
    num1=int(input("Enter the num1: "))
    num2=int(input("Enter the num2: "))

    Addition = ArithmaticModule.Add(num1,num2)
    print("Addition is: ",Addition)
    Substraction = ArithmaticModule.Sub(num1,num2)
    print("Substraction is: ",Substraction)
    Multiplication = ArithmaticModule.Multiply(num1,num2)
    print("Multiplication is: ",Multiplication)
    Division = ArithmaticModule.Divide(num1,num2)
    print("Division is: ",Division)
    
if __name__ =="__main__":
    main()