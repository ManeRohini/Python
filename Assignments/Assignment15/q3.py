#3.Write a lambda function using filter() 
# which accepts a list of numbers and returns a list of odd numbers.

Odd_num = lambda No: (No%2 !=0) 

def main():
    Data=[13,12,8,10,11,20]
    print("Input data is :",Data)

    print("Data before  ",Data)

    FData=list(filter(Odd_num,Data))
    
    print("Data after  ",FData)

if __name__ =="__main__":
    main()