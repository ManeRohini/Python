#1.Write a lambda function which accepts one number and returns square of that number.

square = lambda No: No*No

def main():
    Num =int(input("Enter the number: "))
    result =square(Num)
    print("The suare of num is: ", result)

if __name__ =="__main__":
      main()  