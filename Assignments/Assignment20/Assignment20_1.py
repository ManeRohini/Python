"""
1: Design a Python application that creates two separate threads named Even and Odd.

The Even thread should display the first 10 even numbers.

The Odd thread should display the first 10 odd numbers.

Both threads should execute independently using the threading module.

Ensure proper thread creation and execution.
"""
import threading

def Even(no):
    even_list = []
    for i in range(2,no+1):
        if(i%2 ==0):
            even_list.append(i)
    print("even no in list is :",even_list)    
    return even_list

def Odd(no):
    odd_list = []
    for i in range(1,no+1):
        if(i%2 !=0):
            odd_list.append(i)
    print("odd no in list is:",odd_list)
    return odd_list

def main():
   # values = [int(x) for x in input("Enter the numbers separated by space: ").split()]
    t1=threading.Thread(target=Even, args=(20,))
    t2=threading.Thread(target=Odd, args=(20,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__=="__main__":
    main()