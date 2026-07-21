def Calc(No1,No2):
    Mult = No1*No2
    Div = No1 / No2
    return Mult, Div

def main():
    Value1 = int(input("Enter 1st num: "))
    Value2 = int(input("Enter 2nd num: "))

    Ret1 , Ret2 = Calc(Value1, Value2)
    print("Multiplication is :", Ret1)
    print("Division is: ", Ret2)

if __name__ =="__main__":
    main()
