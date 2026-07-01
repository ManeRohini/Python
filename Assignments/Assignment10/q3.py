#3. Write a program which accepts one number and prints factorial of that number.
#Input: 5
#Output: 120

def Factorial(No):
    fact=1
    for i in range(1,No+1):
        fact *= i
        
    print("The Factorial is", fact)


def main():
    num=int(input("Enter the number: "))
    Factorial(num)


if __name__=="__main__":
    main()