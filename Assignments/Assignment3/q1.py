# what is user defined function?
#User defined function is the function written by the user or developer to perform a perticular task, that can return any desired value of ,inside function it can perform any logic

# write a function that accept 2 numbers and return their multiplication

def multiplication(num1, num2):
    result = num1 * num2
    return result
  

def main():

    a = int(input("Enter 1st number: "))
    print("value of no1: ", a)

    b = int(input("Enter 2nd number: "))
    print("value of no2: ", b)

    multiply = multiplication(a,b)
    print("Result of multiplication is : ", multiply)

if __name__ =="__main__":
    main()





