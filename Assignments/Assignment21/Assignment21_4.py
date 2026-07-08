"""
4: Design a Python application that creates two threads.

Thread 1 should compute the sum of elements from a list.

Thread 2 should compute the product of elements from the same list.

Return the results to the main thread and display them.
"""
import threading

def Thread1(lst):
    sum=0
    for i in lst:
        sum+=i
    print("sum is: ", sum)
    return sum

def Thread2(lst):
    product=1
    for i in lst:
        product*=i
    print("product is: ", product)
    return product
    
def main():
    values = [int(x) for x in input("Enter the numbers separated by space: ").split()]
    t1=threading.Thread(target=Thread1, args=(values,))
    t2=threading.Thread(target=Thread2, args=(values,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__=="__main__":
    main()