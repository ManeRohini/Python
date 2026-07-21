CheckEven = lambda no: (no % 2==0)

def main():
    value =int(input("Enter number: "))
    Ret=CheckEven(value)  #after compilation Ret=(value %2==0)

    if(Ret==True):
        print("it's even number")
    else:
        print("it's odd number")


if __name__=="__main__":
    main()