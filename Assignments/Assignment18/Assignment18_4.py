"""
4. Write a program which accept N numbers from user and store it into List. 
Accept one another number from user and return frequency of that number from List.

Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
"""
def FrequencyOfNumInList(lst,num):
    count = 0
    for i in lst:                 
        if i==num:
            count+=1         
    return count
    
def main():
    num=int(input("Enter the count of  number of elements: "))

    values = list(map(int, input(f"Enter {num} elements separated by space: ").split()))

    no=int(input("Enter the number of to check frequency of that no in list: "))

    ret=FrequencyOfNumInList(values,no)

    print(f"The FrequencyOfNumInList is: ", ret)
    
if __name__ =="__main__":
    main()