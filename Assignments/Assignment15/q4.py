#4.Write a lambda function using reduce() which accepts a list 
# of numbers and returns the addition of all elements.

from functools import reduce

add_lst = lambda No1,No2: No1+No2

def main():
    Data=[13,12,8,10,11,20]
    print("Input data is :",Data)

    RData=(reduce(add_lst,Data))
    
    print("Addition is ",RData)

if __name__ =="__main__":
    main()