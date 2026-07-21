import os
import time
import multiprocessing

#2+4+6+8 =20
def SumEven(no):
    print(f"PID of SumEven: {os.getpid()} PPID of SumEven: {os.getppid()}")
    sum=0
    for i in range(2,no,2):
        sum=sum+i

    print("sum of even is :",sum)

#1+3++5+7+9=25
def SumOdd(no):
    print(f"PID of SumOdd: {os.getpid()} PPID of SumOdd: {os.getppid()}")

    sum=0
    for i in range(1,no,2):
        sum=sum+i

    print("sum of odd is :",sum)

def main():
    print(f"PID of main: {os.getpid()} PPID of main: {os.getppid()}")

    start_time=time.perf_counter()
    t1=multiprocessing.Process(target=SumEven, args=(100,))
    t2=multiprocessing.Process(target=SumOdd, args=(100,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end_time=time.perf_counter()

    print(f"Time required: {end_time - start_time:.4f}")

if __name__=="__main__":
    main()