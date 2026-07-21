

def main():
    Ans = 0 
    try:
        print("Enter 1st number: ")
        No1 = int(input())

        print("Enter 2nd number: ")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is successfull ")

    except ZeroDivisionError as zobj:
        print("Exception occured due to second operend is zero: " ,zobj)

    except ValueError as vobj:
        print("Exception occured due to invalid data type: " ,vobj)

    print("Division is: ",Ans)

if __name__ == "__main__":
    main()