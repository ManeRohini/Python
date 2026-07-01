#1. Write a program which accepts length and width of rectangle and prints area.

def RectArea(length,width):
    Area = length * width
    print("Area of rectangle is: ",Area)

def main():
    print("This program calculates area of rectangle")
    len=int(input("Enter the length:"))
    wid=int(input("Enter the width:"))

    RectArea(len,wid)

if __name__ =="__main__":
    main()

