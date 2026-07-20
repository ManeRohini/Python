""""
4. Write a program that calculates
1^5+2^5+3^5+....+n^5
for multiple values of N simultaneously using Pool.

Input
1000000,
2000000,
3000000,
4000000
Measure total execution time.

"""

import time

def RaiseTo5(No):
    Sum=0
    for i in range(1,No+1):
        Sum = Sum + (i**5)
    return Sum

def main():
    Data=[1000000,2000000,3000000,4000000,5000000]
    Result=[]

    start_time=time.perf_counter()
    for value in Data:
        Ret=RaiseTo5(value)
        Result.append(Ret)

    end_time=time.perf_counter()

    print("Result is: ")
    print(Result)
    print(f"Time required is: {end_time - start_time:.4f} secs")

if __name__ =="__main__":
    main()