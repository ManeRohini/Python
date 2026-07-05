#7.Write a lambda function which accepts one number and returns True if divisible by 5.

Divisible_by_5 = lambda No: True if No %5==0 else False

def main():
    Num =int(input("Enter the number: "))
    result =Divisible_by_5(Num)
    print("The num is Divisible_by_5 or not?: ", result)

if __name__ =="__main__":
      main() 