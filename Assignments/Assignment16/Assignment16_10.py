

#10. Write a program which accepts a name from the user and displays the length of its name.
#Input: Marvellous  Output: 10

def Print(Name):
    length=len(Name)
    print(length)
    

def main():
    name=input("Enter the name: ")
    Print(name)
    
    
if __name__ =="__main__":
    main()