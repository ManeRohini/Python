#6 : 1*2*3*4*5*6
import time

def factorial(No):
    fact=1
    for i in range(1,No+1):
        fact = fact *i

    return fact

def main():
    value =int(input("Enter number:"))

    start_time=time.perf_counter()
    Ret = factorial(value)
    end_time=time.perf_counter()

    print(f"Factorial of {value} is {Ret}") #this is formated printing
    print(f"Time required is : {end_time - start_time:.5f} seconds")

if __name__=="__main__":
    main()