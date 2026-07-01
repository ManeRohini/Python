#3. Write a program which accepts one number and prints square of that number.  
#Input: 5
#Output: 25

def Square(No):
    Sqr = No *No
    print("The square of number ",No ,"is ",Sqr)


def main():
    Num =int(input("Enter the number: "))
    Square(Num)

if __name__ =="__main__":
    main()