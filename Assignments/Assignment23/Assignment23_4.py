""""
4: Write a program that counts how many odd numbers exist between 1 and N.

Input  
Data = [1000000, 2000000, 3000000, 4000000]

Expected Output Format  
Process ID : 1237
Input Number : 1000000
Odd Number Count : 500000
"""
import os
import multiprocessing


def count_odds(N):
    count = 0
    for i in range(1, N + 1):
        if i % 2 != 0:  
            count += 1
    pid = os.getpid()
    return (pid, N, count)


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()
    results = pobj.map(count_odds, Data)

    for pid, n, counts in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {n}")
        print(f"SumOdd : {counts}")
        print("-" * 40)

    print("Main Process ID :", os.getpid())

if __name__ == "__main__":
    main()