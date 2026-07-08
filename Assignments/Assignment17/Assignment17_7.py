"""
7. Write a program which accepts one number and displays the below pattern.
Input: 5
Output:
1 2 3 4 5  
1 2 3 4 5  
1 2 3 4 5  
1 2 3 4 5  
1 2 3 4 5

"""""

def Display(No):
    for i in range(1, No+1):   
        for j in range(1, No+1):     
         print(j, end=" " ) 
        print()
   
    
def main():
    num=int(input("Enter the value: "))
    Display(num)
    
if __name__ =="__main__":
    main()