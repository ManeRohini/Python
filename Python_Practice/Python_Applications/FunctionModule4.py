from Marvellous import Addition, Substraction

def main():
    print("Enter 1st number: ")
    value1 = int(input())

    print("Enter 2st number: ")
    value2 = int(input())

    ret = Addition(value1, value2) 
    print("Addition is: ", ret)

    ret1 = Substraction(value1, value2) #Error
    
    print("Addition is: ", ret1)
    
if __name__ == "__main__":
    main()


