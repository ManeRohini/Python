#3.Write a lambda function which accepts two numbers and returns maximum number.

max_num = lambda No1,No2: No1 if No1>No2 else No2

def main():
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))
    result =max_num(Num1,Num2)
    print("The max number is: ", result) 

if __name__ =="__main__":
      main()