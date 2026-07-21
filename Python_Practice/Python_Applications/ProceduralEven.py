def CheckEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False

def main():
    value =int(input("Enter number: "))
    Ret= CheckEven(value)

    if(Ret==True):
        print("it's even number")
    else:
        print("it's odd number")



if __name__=="__main__":
    main()