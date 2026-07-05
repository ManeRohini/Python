#6.Write a lambda function which accepts one number and returns True if number is odd otherwise False.

Odd_num = lambda No: True if (No%2 !=0) else False

def main():
    Num =int(input("Enter the number: "))
    result =Odd_num(Num)
    print("The num is odd True or False ?: ", result)

if __name__ =="__main__":
      main() 