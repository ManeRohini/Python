"""
2: Design a Python application that creates two threads.

Thread 1 should calculate and display the maximum element from a list.

Thread 2 should calculate and display the minimum element from the same list.

The list should be accepted from the user.

"""
import threading

def Thread1(lst):
    max=lst[0]
    for i in lst:
        if(i>max):
            max=i
    print("Max is: ", max)
    return max

def Thread2(lst):
    min=lst[0]
    for i in lst:
        if(i<min):
            min=i
    print("Min is: ", min)
    return min
    
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