#1.Write a lambda function using map() which accepts a 
#list of numbers and returns a list of squares of each number.

from functools import reduce

squares = lambda nums: nums**2

def main():
    Data=[3,5,7]
    print("Input data is :",Data)

    print("Data before  ",Data)

    MData=list(map(squares,Data))
    
    print("Data after  ",MData)

if __name__ =="__main__":
    main()