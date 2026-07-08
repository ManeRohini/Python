#8. Write a program which accepts a number from the user and prints that number of “*” on screen.

def Print(No):
    for i in range(1,No+1):
        print("*", end=" ")
    

def main():
    num=int(input("Enter the value: "))
    Print(num)
    
if __name__ =="__main__":
    main()