#Write a lambda function which accepts two numbers and returns multiplication.

Multiply= lambda No1,No2: No1 *No2

def main():
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))
    result =Multiply(Num1,Num2)
    print("The Multiplication is: ", result) 

if __name__ =="__main__":
      main()