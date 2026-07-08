"""
1: Design a Python application that creates two threads named Prime and NonPrime.

Both threads should accept a list of integers.

The Prime thread should display all prime numbers from the list.

The NonPrime thread should display all non-prime numbers from the list.
"""
import threading

def Prime(lst):
    prime_list = []
    for num in lst:
        if num > 1:  
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
    print("Prime list is :",prime_list)    
    return prime_list

def NonPrime(lst):
    Nonprime_list = []
    for num in lst:
        if num > 1:  
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0: 
                    Nonprime_list.append(num)
                    break
        else:
            Nonprime_list.append(num) #for 0,1
                       
    print("NonPrime list is :",Nonprime_list)    
    return Nonprime_list

def main():
    values = [int(x) for x in input("Enter the numbers separated by space: ").split()]
    t1=threading.Thread(target=Prime, args=(values,))
    t2=threading.Thread(target=NonPrime, args=(values,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__=="__main__":
    main()