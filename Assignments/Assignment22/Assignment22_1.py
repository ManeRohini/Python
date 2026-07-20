""""
1. Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

Example Input  
[1000000, 2000000, 3000000, 4000000]

Expected Output  
[333333833333500000, 2666668666666700000, ...]

"""
import multiprocessing
from multiprocessing import Pool


def SumSquare(No):
    Sum=0
    for i in range(1,No+1):
        Sum = Sum + (i**2)
    return Sum

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    pobj =multiprocessing.Pool()
    results = pobj.map(SumSquare, numbers)

    print("Input:", numbers)
    print("Output:", results)

if __name__ == "__main__":
    main()