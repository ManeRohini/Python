#What happens if the number of arguments passed does not match the function parameters?


def Add(a,b):
    sum=a+b
    return sum

def main():
    ret=Add(5,4) # no error as no. of aruments passed to function call are same as function parameters

    ret2=Add(8) #error no of arguments < no. of parameters

    rer3=Add(1,2,3)  #error no.of arguments > no of parameters


if __name__ =="__main__":
    main()

"""
  File "C:\Users\Admin\Desktop\PYAssignments\Assignment6\q8.py", line 17, in <module>
    main()
    ~~~~^^
  File "C:\Users\Admin\Desktop\PYAssignments\Assignment6\q8.py", line 11, in main
    ret2=Add(8) #error no of arguments < no. of parameters
TypeError: Add() missing 1 required positional argument: 'b'

"""