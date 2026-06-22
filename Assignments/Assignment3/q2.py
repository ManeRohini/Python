#what is the difference between function with parameter and function without parameter?
#if user pass some input variables to the function then it is called as a function with parameter
# if we do not pass any input variables to the function then it is called as function without parameter

#example_1:
# function with parameter
def Addition(no1,no2):
    add=no1+no2
    return add
    
# function without parameter
def main():
    a = int(input("Enter 1st number: "))
    print("value of no1: ", a)

    b = int(input("Enter 2nd number: "))
    print("value of no2: ", b)

    Sum = Addition(a,b)
    print("Result of Addition is : ", Sum)

if __name__ =="__main__":
    main()


#example_2:

# function without parameter

def name():
    print("enter your mane: ")
    name =input()

    print("Student name is: ", name)

name()


