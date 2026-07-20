""""
5: Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.

Input  
Data = [10, 15, 20, 25]

Expected Task  
For every N, calculate:
N!

Expected Output Format  
Process ID : 1240
Input Number : 20
Factorial : 2432902008176640000
"""
import os
import multiprocessing


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    pid = os.getpid()   # get process ID
    return (pid, n, result)


def main():
    Data = [10, 15, 20, 25]

    pobj = multiprocessing.Pool()
    results = pobj.map(factorial, Data)

    for pid, n, fact in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {n}")
        print(f"Factorial : {fact}")
        print("-" * 40)

    print("Main Process ID :", os.getpid())

if __name__ == "__main__":
    main()