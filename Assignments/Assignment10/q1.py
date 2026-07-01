#1. Write a program which accepts one number and prints multiplication table of that number.
#Input:4
#output:4 8 12 16 20 24 28 32 36 40

def Table(no):
    print("Multiplication Table of", no)
    total = 0
    for i in range(1, 11): 
        product =  no * i 
        print( product, end=" ")
        total +=product
    #print("Total is: ",total)

    
def main():
    num=int(input("Enter the number: "))
    Table(num)


if __name__=="__main__":
    main()