#6.Write a lambda function using reduce() which accepts 
# a list of numbers and returns the minimum element.



add_lst = lambda No1,No2: No1 if No1<No2 else No2

def main():
    Data=[13,12,8,10,11,20]
    print("Input data is :",Data)

    FData=int(filter(add_lst,Data))
    
    print("Min is  ",FData)

if __name__ =="__main__":
    main()