#4. Write a program which accepts one number and prints binary equivalent.

def ConvertToBinary(No):
    Binary=[]
    while No>0:
        remainder =No%2
        Binary.append(remainder)
        No=No//2
    Binary.reverse()
    return Binary

def main():
    num =int(input("Enter the number:"))
    FinalBinary=ConvertToBinary(num)
    print("The ",num, "in Binary is: ", FinalBinary)

if __name__ =="__main__":
    main()