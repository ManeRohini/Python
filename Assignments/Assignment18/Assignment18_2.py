"""
2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
"""

def MaxInList(lst):
    max = lst[0]
    for i in lst:                 
        if i>max:
            max=i          
    return max
    
def main():
    num=int(input("Enter the count of  number of elements: "))

    values = list(map(int, input(f"Enter {num} elements separated by space: ").split()))

    ret=MaxInList(values)

    print(f"Max is: ", ret)
    
if __name__ =="__main__":
    main()