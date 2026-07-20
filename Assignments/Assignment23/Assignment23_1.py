""""
1: Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.

Input  
Data = [1000000, 2000000, 3000000, 4000000]

Expected Task  
For each number N, calculate:
2 + 4 + 6 + … + N

Expected Output Format  
Process ID : 1234
Input Number : 1000000
Sum of Even Numbers : 250000500000
"""
import time
import os
import multiprocessing

def SumEven(no):
   
    total = (no // 2) * ((no // 2) + 1)
    pid = os.getpid()
    return (pid, no, total)

def main():
    Data = [1000000, 2000000, 3000000, 4000000, 5000000]

    start_time = time.perf_counter()

    # Parallel execution
    pobj = multiprocessing.Pool()
    results = pobj.map(SumEven, Data)

    end_time = time.perf_counter()

    # Display results
    for pid, n, total in results:
        print(f"Process ID of SumEven: {pid}")
        print(f"Input Number : {n}")
        print(f"Sum of Even Numbers : {total}")
        print("-" * 40)

    print("Main Process ID :", os.getpid())
    print(f"Time required is: {end_time - start_time:.4f} secs")

if __name__ == "__main__":
    main()
