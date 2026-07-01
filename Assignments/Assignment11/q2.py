#2. Write a program which accepts one number and prints count of digits in that number.  
#Input: 7521
#Output: 4

def CountDigit(No):
    count =0
    while No>0:
        No=No //10
        count +=1
    return count

def main():
    num=int(input("Enter the number: "))
    Result=CountDigit(num)
    print("Count of digits in", num, "is:", Result)


if __name__=="__main__":
    main()