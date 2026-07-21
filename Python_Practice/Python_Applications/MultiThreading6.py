import time

#2+4+6+8 =20
def SumEven(no):
    sum=0
    for i in range(2,no,2):
        sum=sum+i

    print("sum of even is :",sum)

#1+3++5+7+9=25
def SumOdd(no):
    sum=0
    for i in range(1,no,2):
        sum=sum+i

    print("sum of odd is :",sum)


def main():
    start_time=time.perf_counter()
    SumEven(1000000000)
    SumOdd(1000000000)
    end_time=time.perf_counter()

    print(f"Time required: {end_time - start_time:.4f}")


if __name__=="__main__":
    main()