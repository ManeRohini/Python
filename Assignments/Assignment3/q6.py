#write program to dispaly data type, mem address, size in bytes of variable entered by the user

import sys


def display(a):
    print("Enter the value: ")

    a= input()

    print(a)
    print(id(a))
    print(type(a))
    print(sys.getsizeof(a))


display(5)   