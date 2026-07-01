#3. Write a program which accepts one number and checks whether it is perfect number or not.  
#Input: 6
#Output: Perfect Number

def IsPerfectNo(No):
    sum=0
    for i in range(1, No):
        if No%2 ==0:
             sum +=i
    return sum==No

def main():
    num =int(input("Enter the number to check if it is perfect number or not:"))
    result=IsPerfectNo(num)
    
    if True:
        print("The number is perfect number")
    else:
        print("The number is not a perfect number")

if __name__ =="__main__":
    main()
