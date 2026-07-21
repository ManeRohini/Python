#6 : 1*2*3*4*5*6

def factorial(No):
    fact=1
    for i in range(1,No+1):
        fact = fact *i

    return fact

def main():
    value =int(input("Enter number:"))

    Ret = factorial(value)

    print(f"Factorial of {value} is {Ret}") #this is formated printing

if __name__=="__main__":
    main()