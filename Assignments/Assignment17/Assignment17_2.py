""""
2. Write a program which accepts one number and displays the below pattern.
Input: 5
Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

"""
def Display(No):
    for i in range(1, No+1):       
        print("* " * No) 
   
    
def main():
    num=int(input("Enter the value: "))
    Display(num)
    
if __name__ =="__main__":
    main()