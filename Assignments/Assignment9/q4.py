#4. Write a program which accepts one number and prints cube of that number.

def Cube(No):
    cube = No*No*No
    print("The cube of number ",No ,"is ",cube)


def main():
    Num =int(input("Enter the number: "))
    Cube(Num)

if __name__ =="__main__":
    main()