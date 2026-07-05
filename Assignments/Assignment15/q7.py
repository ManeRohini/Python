#7.Write a lambda function using filter() which accepts a list of strings 
# and returns a list of strings having length greater than 5.

GreaterThan5 = lambda str: len(str)>5 

def main():
    Data=["I","am","Marvellous","student"]
    print("Input data is :",Data)

    FData=list(filter(GreaterThan5,Data))
    
    print("GreaterThan5 is  ",FData)

if __name__ =="__main__":
    main()