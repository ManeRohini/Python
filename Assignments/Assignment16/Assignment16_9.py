#9. Write a program which displays the first 10 even numbers on screen.
#Output: 2 4 6 8 10 12 14 16 18 20

def Print(No):
    for i in range(2,No+1,2):
        print(i, end=" ")
    

def main():
    num=int(input("Enter the value: "))
    Print(num)
    
if __name__ =="__main__":
    main()