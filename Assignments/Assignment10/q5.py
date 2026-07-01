#5. Write a program which accepts one number and prints all odd numbers till that number.

def Odd(No):
    for i in range(1,No+1):
        if i % 2 != 0:
            print(i, end =" ")
        

def main():
    num=int(input("Enter the number: "))
    Odd(num)

if __name__=="__main__":
    main()