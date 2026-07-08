""""
#6. Write a program which accepts one number and displays the below pattern.
#Input: 5
#Output:
* * * * *
* * * *
* * *
* *
*
"""

def Display(No):
    for i in range(No, 0, -1):       
        print("* " * i) 
   
    
def main():
    num=int(input("Enter the value: "))
    Display(num)
    
if __name__ =="__main__":
    main()