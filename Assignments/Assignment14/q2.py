#2.Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda No: No**3

def main():
    Num =int(input("Enter the number: "))
    result =Cube(Num)
    print("The cube of num is: ", result)

if __name__ =="__main__":
      main()  