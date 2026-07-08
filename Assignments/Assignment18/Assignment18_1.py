"""
1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
"""

def ListAdd(lst):
    total = 0
    for i in lst:                 
        total += i            
    return total
    
def main():
    num=int(input("Enter the count of  number of elements: "))

    values = list(map(int, input(f"Enter {num} elements separated by space: ").split()))

    ret=ListAdd(values)

    print(f"ListAdd of {num} numbers, which is entered by user is : {ret}")
    
if __name__ =="__main__":
    main()