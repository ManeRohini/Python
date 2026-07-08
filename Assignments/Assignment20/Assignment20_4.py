""""
4: Design a Python application that creates three threads named Small, Capital, and Digits.

All threads should accept a string as input.

The Small thread should count and display the number of lowercase characters.

The Capital thread should count and display the number of uppercase characters.

The Digits thread should count and display the number of numeric digits.

Each thread must also display:

Thread ID

Thread Name

"""
import threading

def Small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1    
    print(f"Thread ID: {threading.get_ident()}, Thread Name: {threading.current_thread().name}")
    print("Number of lowercase characters:", count)

def Capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1 
    print(f"Thread ID: {threading.get_ident()}, Thread Name: {threading.current_thread().name}")
    print("Number of uppercase characters:", count)

def Digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1 
    print(f"Thread ID: {threading.get_ident()}, Thread Name: {threading.current_thread().name}")
    print("Number of digits:", count)

def main():
    print(f"Thread ID: {threading.get_ident()}, Thread Name: {threading.current_thread().name}")    
    str = input("Enter a string having char and num: ")
    t1=threading.Thread(target=Small, args=(str,))
    t2=threading.Thread(target=Capital, args=(str,))
    t3=threading.Thread(target=Digits, args=(str,))

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("Exit from main")

if __name__=="__main__":
    main()