#10. Write a lambda function which accepts three numbers and returns largest number.

Largest_num = lambda a, b, c: max(a, b, c)

def main():
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))
    Num3 = int(input("Enter the third number: "))
    
    result =Largest_num(Num1,Num2,Num3)
    print("The max number is: ", result) 

if __name__ =="__main__":
      main()