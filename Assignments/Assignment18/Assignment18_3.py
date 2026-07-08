"""
3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5
"""

def MinInList(lst):
    min = lst[0]
    for i in lst:                 
        if i<min:
            min=i          
    return min
    
def main():
    num=int(input("Enter the count of  number of elements: "))

    values = list(map(int, input(f"Enter {num} elements separated by space: ").split()))

    ret=MinInList(values)

    print(f"Min is: ", ret)
    
if __name__ =="__main__":
    main()