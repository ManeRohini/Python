""""
2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().

Input  
[10, 15, 20, 25]

Display

Process ID

Input Number

Factorial

"""
import os
import time
import multiprocessing
from multiprocessing import Pool

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result =result * i
    return result


def main():
    numbers = [10, 15, 20, 25]
    
    pobj =multiprocessing.Pool()
    results = pobj.map(factorial, numbers)

    print("Input:", numbers)
    print("Output:", results)

if __name__ == "__main__":
    main()