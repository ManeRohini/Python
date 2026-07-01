#4. Write a program which accepts one number and prints reverse of that number.  
#Input: 123
#output:321

def ReverseNo(No):
    rev=0
    while No>0:
        digit=No%10
        rev= rev*10+digit
        No=No//10
    return rev

def main():
    num=int(input("Enter the number: "))
    Result=ReverseNo(num)
    print("Reverse of digits in", num, "is:", Result)


if __name__=="__main__":
    main()