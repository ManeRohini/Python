"""
9. Write a program which accepts a number from the user and returns the number of digits in that number.
Input: 5187934  Output: 7
"""

def Display(No):
    count=0
    while No>0:
        count=count+1
        No=No//10
    return count
   
    
def main():
    num=int(input("Enter the value: "))
    CountNum=Display(num)
    print("Total digit in number is: ",CountNum)
    
if __name__ =="__main__":
    main()