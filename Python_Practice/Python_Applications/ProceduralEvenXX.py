def CheckEven(no):
   return (no % 2==0)


def main():
    value =int(input("Enter number: "))
    Ret=CheckEven(value)

    if(Ret==True):
        print("it's even number")
    else:
        print("it's odd number")


if __name__=="__main__":
    main()