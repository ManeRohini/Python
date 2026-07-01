#2. Write a program which accepts one number and prints sum of first N natural number
#Input: 5
#Output: 15

def SumNaturalNo(No):
    for i in range(1,No):
        No=No+i
    print("The sum of natural numbers is", No)


def main():
    num=int(input("Enter the number: "))
    SumNaturalNo(num)


if __name__=="__main__":
    main()