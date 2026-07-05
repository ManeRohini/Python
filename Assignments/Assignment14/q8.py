#8.Write a lambda function which accepts two numbers and returns addition.

Addition= lambda No1,No2: No1 +No2

def main():
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))
    result =Addition(Num1,Num2)
    print("The Addition is: ", result) 

if __name__ =="__main__":
      main()