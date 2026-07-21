def CheckEven(no):
    if(no % 2 == 0):
        print("It's even number")
    else:
        print("It's odd number")


def main():
    value =int(input("Enter number: "))
    CheckEven(value)


if __name__=="__main__":
    main()