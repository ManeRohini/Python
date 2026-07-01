#5. Write a program which accepts one number and checks whether it is divisible by 3 and 5.  
#Input: 15
#Output: Divisible by 3 and 5

def DivBy3and5(No):
    if(No %3 ==0 and No %5 == 0):
        print("The number is divisible by 3 and 5")
    else:
        print("The number is not divisible by 3 and 5")

def main():
    Num = int(input("Enter the number: "))
    DivBy3and5(Num)

if __name__ =="__main__":
    main()
 
    