"""
2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.

Input : 4  3  Output : 12
Input : 6  3  Output : 18
"""
add = lambda no1,no2: no1+no2

def main():
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))

    ret=add(num1,num2)

    print(f"The power is: ", ret)
    
if __name__ =="__main__":
    main()