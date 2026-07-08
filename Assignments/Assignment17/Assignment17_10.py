"""
10. Write a program which accepts a number from the user and returns the addition of digits in that number.
Input: 5187934  Output: 37
"""

def Display(No):
    sum=0
    while No>0:
        digit=No%10
        sum=sum+digit
        No=No//10
    return sum
   
def main():
    num=int(input("Enter the value: "))
    CountNum=Display(num)
    print("Total digit in number is: ",CountNum)
    
if __name__ =="__main__":
    main()