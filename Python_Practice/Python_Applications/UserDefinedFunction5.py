#Accept: multiple parameter
#Return: multiple value

def Marvellous(Value1, Value2):
    print("Inside Marvellous: ", Value1, Value2)
    return 21,51     

def main():
    print("Inside main")
    ret1, ret2 = Marvellous(10,20)
    print("return values are: ", ret1, ret2)
 
if __name__ =="__main__":
    main()


