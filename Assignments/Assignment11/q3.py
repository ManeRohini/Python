#3. Write a program which accepts one number and prints sum of digits.  
#Input: 123
#Output: 6

def SumDigit(No):
    Sum =0
    while No>0:
        digit=No % 10
        Sum +=digit
        No=No//10
    return Sum

def main():
    num=int(input("Enter the number: "))
    Result=SumDigit(num)
    print("Sum of digits in", num, "is:", Result)


if __name__=="__main__":
    main()