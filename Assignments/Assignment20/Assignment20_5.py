"""
5: Design a Python application that creates two threads named Thread1 and Thread2.

Thread1 should display numbers from 1 to 50.

Thread2 should display numbers from 50 to 1 in reverse order.

Ensure that:

Thread2 starts execution only after Thread1 has completed.

Use appropriate thread synchronization.

"""
import threading

def Thread1(no):
    for i in range(1,no+1):
        print(i, end =" ")    

def Thread2(no):
    for i in range(no,0,-1):
        print(i, end =" ") 

def main():
    num =int(input("Enter the no: "))
    t1=threading.Thread(target=Thread1, args=(num,))
    t2=threading.Thread(target=Thread2, args=(num,))

    t2.start()
    t2.join()
    print()
    t1.start()
    t1.join()
    

if __name__=="__main__":
    main()