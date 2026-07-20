""""
2: Write a Python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N.

Input  
Data = [1000000, 2000000, 3000000, 4000000]

Expected Task  
For each number N, calculate:
1 + 3 + 5 + … + N

Expected Output Format  
Process ID : 1235
Input Number : 1000000
Sum of Odd Numbers : 250000000000
"""
import time
import os
import multiprocessing

#1+3++5+7+9=25
def SumOdd(no):
    print(f"PID of SumOdd: {os.getpid()} PPID of SumOdd: {os.getppid()}")

    sum=0
    for i in range(1,no,2):
        sum=sum+i

    print("sum of odd is :",sum)

def main():
    print(f"PID of main: {os.getpid()} PPID of main: {os.getppid()}")

    Data = [1000000, 2000000, 3000000, 4000000, 5000000]
    start_time=time.perf_counter()

    pobj = multiprocessing.Pool()
    results = pobj.map(SumOdd, Data)

    end_time=time.perf_counter()

    print(f"Time required: {end_time - start_time:.4f}")

if __name__=="__main__":
    main()