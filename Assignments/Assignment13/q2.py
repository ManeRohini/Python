#2. Write a program which accepts radius of circle and prints area of circle.

def CircleArea(radious, Pi=3.14):
    Area = Pi*radious*radious
    print("The area of circle is: ",Area)

def main():
    print("This program calculates area of circle")
    radious=int(input("Enter the radious:"))
    CircleArea(radious)
    CircleArea(radious,6.28)

if __name__ =="__main__":
    main()

