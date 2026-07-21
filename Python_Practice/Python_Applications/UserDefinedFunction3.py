#Accept: 1 parameter
#Return: 1 value

def Marvellous(Value):
    print("Inside Marvellous: ", Value)
    return 21
     

def main():
    print("Inside main")
    ret = Marvellous(11)
    print("value of ret: ", ret)
 

if __name__ =="__main__":
    main()


