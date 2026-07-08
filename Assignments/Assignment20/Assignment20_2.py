"""
2: Design a Python application that creates two threads named EvenFactor and OddFactor.

Both threads should accept one integer number as a parameter.

The EvenFactor thread should:

Identify all even factors of the given number.

Calculate and display the sum of even factors.

The OddFactor thread should:

Identify all odd factors of the given number.

Calculate and display the sum of odd factors.

After both threads complete execution, the main thread should display the message:  
“Exit from main”

"""

import threading

def EvenFactor(no):
    even_factors = []
    for i in range(1, no+1):
        if no % i == 0 and i % 2 == 0:
            even_factors.append(i)
    print("Even factors:", even_factors)
    print("Sum of even factors:", sum(even_factors))

def OddFactor(no):
    odd_factors = []
    for i in range(1, no+1):
        if no % i == 0 and i % 2 != 0:
            odd_factors.append(i)
    print("Odd factors:", odd_factors)
    print("Sum of odd factors:", sum(odd_factors))

def main():
    num = int(input("Enter an integer number: "))

    t1=threading.Thread(target=EvenFactor, args=(num,))
    t2=threading.Thread(target=OddFactor, args=(num,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Exit from main")

if __name__=="__main__":
    main()