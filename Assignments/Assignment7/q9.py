#Why do we write the condition: if __name__ == "__main__":

#in python code if file is executed directly the __name__ gives __main as return
#we add if __name__ ="__main__" , to call main function
#we use this above if condition to have a code execution start point

#Example:

def Show():
    print("welcome...!!!")

def main():
    Show()

if __name__ =="__main__":
    main()    
    
